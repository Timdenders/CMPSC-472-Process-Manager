import logging
import multiprocessing
import os
import psutil
import random
import threading
import time

# Configure logging for the process manager and set log file name
logging.basicConfig(filename='proc_mgr_log.log',
                    level=logging.INFO, format='%(asctime)s - %(message)s')
process_mgr_log = logging.getLogger('proc_mgr_log')
process_mgr_log.setLevel(logging.INFO)

# Define constants and data structures for process and thread management
BUFFER_SIZE = 5
buffer = []
mutex = threading.Semaphore(1)
empty = threading.Semaphore(BUFFER_SIZE)
data = threading.Semaphore(0)
active_processes = {}
threads_dic = {}
exit_thread = threading.Event()
read_pipe, write_pipe = os.pipe()


# Function to create a new process
def create_process(proc_name):
    try:
        pid = multiprocessing.Process(args=(proc_name,))
        if pid == 0:
            try:
                os.execlp(proc_name, proc_name)
            except Exception as e:
                process_mgr_log.error(
                    f"Process: '{proc_name}', PID: {os.getpid()} error: {str(e)}")
            exit(1)
        else:
            active_processes[pid] = proc_name
            process_mgr_log.info(
                f"Process '{proc_name}', PID: {pid} created")
            process_handler(proc_name)
    except Exception as e:
        process_mgr_log.error(f"Error in create_process: {str(e)}")


# Function to create a new thread
def create_thread(thd_name):
    try:
        process_pid = os.getpid()
        thread = threading.Thread(args=(thd_name,))
        thread.daemon = True
        thread.name = thd_name
        thread.start()
        threads_dic.setdefault(process_pid, []).append(thread)
        process_mgr_log.info(f"Thread '{thd_name}' created")
    except Exception as e:
        process_mgr_log.error(f"Error in create_thread: {str(e)}")


# Function to handle user interactions within a process
def process_handler(proc_name):
    try:
        process_mgr_log.info(
            f"Process: '{proc_name}',  PID: {os.getpid()} running")
        threads_dic[os.getpid()] = []
        while True:
            print("\nOptions:")
            print("(1)  Create a new thread")
            print("(2)  List threads")
            print("(3)  Return")
            cho = input("\nEnter an option number: ")
            if cho == "1":
                thd_name = input("Enter a thread name: ")
                create_thread(thd_name)
            elif cho == "2":
                show_threads()
            elif cho == "3":
                print("\n")
                break
            else:
                print("Please enter a valid number.")
    except Exception as e:
        process_mgr_log.error(f"Error in process_handler: {str(e)}")


# Function to handle user interactions within a thread
def thread_handler(thd_name):
    try:
        while not exit_thread.is_set():
            process_mgr_log.info(f"Thread '{thd_name}' running")
            time.sleep(1)
    except Exception as e:
        process_mgr_log.error(f"Error in thread_handler: {str(e)}")


# Function to display the list of running processes
def show_processes():
    try:
        if not active_processes:
            print("No processes were created")
            process_mgr_log.info("No processes were created")
        else:
            for pid, proc_name in active_processes.items():
                process_info = psutil.Process(pid.pid)
                parent_pid = process_info.ppid()
                state = process_info.status()
                process_mgr_log.info(
                    f"Process: {proc_name}, PID: {pid.pid}, Parent PID: {parent_pid}, State: {state}")
                print(
                    f"Process: {proc_name}, PID: {pid.pid}, Parent PID: {parent_pid}, State: {state}")
    except Exception as e:
        process_mgr_log.error(f"Error in show_processes: {str(e)}")


# Function to display the list of threads within the current process
def show_threads():
    try:
        process_pid = os.getpid()
        thds = threads_dic.get(process_pid, [])
        if not thds:
            print("No threads available from the process.")
        else:
            print(f"Thread name(s): ")
            for thread in thds:
                print(f"{thread.name}", " ", end="")
            print("\n", end="")
    except Exception as e:
        process_mgr_log.error(f"Error in show_threads: {str(e)}")


# Function to terminate a specific process
def terminate_process(p_name):
    for pid, proc_name in list(active_processes.items()):
        if proc_name == p_name:
            process = pid
            if process.is_alive():
                process.terminate()
                del active_processes[pid]
                print(f"Process '{p_name}' terminated")
                process_mgr_log.info(f"Process '{p_name}' terminated")
            else:
                print(f"Process '{p_name}' is not running")
                process_mgr_log.warning(f"Process '{p_name}' is not running")
            return
    print(f"Process '{p_name}' not found.")
    process_mgr_log.error(f"Process '{p_name}' not found.")


# Function to terminate a specific thread
def terminate_thread(thd_name):
    try:
        process_pid = os.getpid()
        thread_terminated = False
        for thread in threads_dic.get(process_pid, []):
            if thread.name == thd_name:
                exit_thread.set()
                thread.join()
                threads_dic[process_pid].remove(thread)
                thread_terminated = True
                print(f"Thread '{thd_name}' terminated")
                process_mgr_log.info(f"Thread '{thd_name}' terminated")
        if not thread_terminated:
            print(f"Thread '{thd_name}' doesn't exist")
            process_mgr_log.error(f"Thread '{thd_name}' doesn't exist")
    except Exception as e:
        process_mgr_log.error(f"Error in terminate_thread: {str(e)}")


# Function to handle user interactions for terminating processes and threads
def terminate_handler():
    try:
        while True:
            print("\nOptions:")
            print("(1)  Terminate a process")
            print("(2)  Terminate a thread")
            print("(3)  Return")
            cho = input("\nEnter an option number: ")
            if cho == "1":
                proc_name = input("Enter a process to terminate: ")
                terminate_process(proc_name)
            elif cho == "2":
                thd_name = input("Enter a thread to terminate: ")
                terminate_thread(thd_name)
            elif cho == "3":
                break
            else:
                print("Please enter a valid number.")
    except Exception as e:
        process_mgr_log.error(f"Error in terminate_handler: {str(e)}")


# Function to send an IPC message
def ipc_send_message(msg):
    try:
        os.write(write_pipe, msg.encode())
        process_mgr_log.info(f"Message sent: {msg}")
    except Exception as e:
        process_mgr_log.error(f"Error in ipc_send_message: {str(e)}")


# Function to receive an IPC message
def ipc_receive_message():
    try:
        if os.fstat(read_pipe).st_size > 0:
            msg = os.read(read_pipe, 512)
            print(f"Received message: {msg.decode()}")
            process_mgr_log.info(f"Received message: {msg.decode()}")
            return msg.decode()
        else:
            print("There are no messages\n")
            process_mgr_log.warning("There are no messages")
    except Exception as e:
        process_mgr_log.error(f"Error in ipc_receive_message: {str(e)}")


# Function to create producer threads for synchronization
def producer(buf, mut, emp, dat):
    for i in range(10):
        item = f"Item {i}"
        emp.acquire()
        mut.acquire()
        buf.append(item)
        print(f"Produced {item}, Buffer: {buf}")
        process_mgr_log.info(f"Produced {item}, Buffer: {buf}")
        mut.release()
        dat.release()
        time.sleep(random.uniform(0.1, 0.5))


# Function to create consumer threads for synchronization
def consumer(buf, mut, emp, dat):
    for i in range(10):
        dat.acquire()
        mut.acquire()
        item = buffer.pop(0)
        print(f"Consumed {item}, Buffer: {buf}")
        process_mgr_log.info(f"Consumed {item}, Buffer: {buf}")
        mut.release()
        emp.release()
        time.sleep(random.uniform(0.1, 0.5))


# Function to perform process synchronization using threads
def synchronize_threads():
    producers = [threading.Thread(target=producer, args=(buffer, mutex, empty, data)) for _ in range(2)]
    consumers = [threading.Thread(target=consumer, args=(buffer, mutex, empty, data)) for _ in range(2)]
    for producer_thread in producers:
        producer_thread.start()
    for consumer_thread in consumers:
        consumer_thread.start()
    time.sleep(3)
    for producer_thread in producers:
        producer_thread.join()
    for consumer_thread in consumers:
        consumer_thread.join()


# Function to display the log text from the log file
def display_log_text():
    try:
        with open('proc_mgr_log.log', 'r') as file:
            log_text = file.read()
            print(log_text)
    except Exception as e:
        logging.error(f"Error in display_log_text: {str(e)}")


if __name__ == "__main__":
    print("An Advanced Process Manager\nwith Process Synchronization")
    print("----------------------------")
    while True:
        print("Options:")
        print("(1)  Create a new process")
        print("(2)  Terminate process/thread")
        print("(3)  List and monitor running processes")
        print("(4)  Send IPC message")
        print("(5)  Receive IPC message")
        print("(6)  Process Synchronization")
        print("(7)  Display log text")
        print("(8)  Exit the program")
        choice = input("\nEnter an option number: ")

        if choice == "1":
            process_name = input("Enter a process name: ")
            create_process(process_name)
        elif choice == "2":
            terminate_handler()
        elif choice == "3":
            show_processes()
        elif choice == "4":
            message = input("Enter a message to deliver: ")
            ipc_send_message(message)
        elif choice == "5":
            received_message = ipc_receive_message()
        elif choice == "6":
            synchronize_threads()
        elif choice == "7":
            display_log_text()
        elif choice == "8":
            print("Exiting program...")
            exit(0)
        else:
            print("Please enter a valid number,\n")
