# Project Title: An Advanced Process Manager with Process Synchronization
Contributor: Timothy D. Enders
## Project Deliverables:
1. Source Code: The source code, provided in a .py file, is accompanied by detailed comments that elucidate the design and implementation.
2. Project Report (README): The project README comprises the following sections:
   - Project Title: Clearly states the title of the project.
   - Implemented Functionalities: Enumerates the functionalities that have been successfully implemented.
   - Installation Instructions: Describes how to install and set up the project.
   - Usage Guide: Provides instructions on how to utilize the project effectively.
   - Test Results: Presents the results of testing each functionality, accompanied by relevant figures and explanatory notes.
   - Project Discussion: Offers an insightful discussion on the outcomes and implications of the project.
## Implemented Functionalities:
1. Process Creation:
   - A mechanism for creating new processes, utilizing system calls such as 'exec'.
2. Process Management:
   - Capabilities to list, terminate, and monitor active processes.
   - Users can access information about each process, including its Process ID (PID), Parent Process ID, and state.
3. Thread Support:
   - The Process Manager can accommodate multiple threads within a process.
   - Contains means for thread creation, termination, and synchronization, leveraging synchronization tools like mutexes and semaphores.
4. Inter-Process Communication (IPC):
   - IPC methods that facilitate communication and data sharing between processes and threads.
   - Techniques such as message passing, shared memory, and pipes for IPC, using system calls like 'pipe'.
5. Process Synchronization:
   - Includes synchronization primitives like mutexes and semaphores.
   - Demonstrates the application of synchronization mechanisms to resolve common synchronization challenges, such as producer-consumer and reader-writer problems.
6. User Interface:
   - A user-friendly interface for interacting with the Process Manager, through a Command-Line Interface (CLI).
   - Allows users to create processes, initiate threads, synchronize threads, and perform IPC operations, all with clear and informative command syntax and options.
7. Logging and Reporting:
   - Features for logging and reporting to track and display the execution of processes and threads.
   - Logs significant events, errors, and information related to process synchronization.
## Installation Instructions:
Before running the program, you need to ensure that you have Python installed on your Windows environment. The code is designed to work in a Windows environment.

Python Installation: If you don't have Python installed, you can download it from the official Python website (https://www.python.org/downloads/) and follow the installation instructions for Windows.

Libraries: This program uses the psutil library for obtaining information about running processes. You can install it using pip:
```shell
pip install psutil
```

Running the Program: To run the program, simply execute the Python script in your terminal or command prompt. Navigate to the directory where the script is located and run:
```shell
python process_manager.py
```

Now, let's move on to the Usage Guide.
## Usage Guide:
This section provides instructions on how to effectively use the Process Manager program. It should guide users on how to perform various actions, create processes, threads, terminate them, and use the different functionalities provided by the program.

1. Creating a New Process:
To create a new process, select option 1.
Enter a unique process name when prompted.
The new process will be created and listed in the active processes.

2. Terminating a Process/Thread:
To terminate a process or thread, select option 2.
Follow the on-screen instructions to specify whether you want to terminate a process or thread and provide the respective name.
The selected process or thread will be terminated.

3. Listing and Monitoring Processes:
To list and monitor running processes, select option 3.
The program will display information about each running process, including its Process ID (PID), Parent Process ID, and state.

4. Sending IPC Message:
To send an Inter-Process Communication (IPC) message, select option 4.
Enter the message you want to send when prompted.
The message will be delivered to the target process or thread.

5. Receiving IPC Message:
To receive an IPC message, select option 5.
The program will check for incoming IPC messages and display them if any are available.

6. Process Synchronization:
To demonstrate process synchronization, select option 6.
The program will execute a demonstration of producer-consumer process synchronization.

7. Display Log Text:
To display the program's log text, select option 7.
You can review the log to check for events, errors, and information related to process synchronization.
Now, let's proceed to the Test Results section.
## Test Results:
Create a new process:

<img src="Test Images/img1.png" alt="Alt Text" width="860" height="350">

Create a new thread and show the list of threads:

<img src="Test Images/img2.png" alt="Alt Text" width="860" height="350">

Show a list of the processes:

<img src="Test Images/img3.png" alt="Alt Text" width="860" height="350">

Terminate a thread:

<img src="Test Images/img4.png" alt="Alt Text" width="860" height="350">

Sending and receiving an IPC Message:

<img src="Test Images/img5.png" alt="Alt Text" width="860" height="350">

Demonstrate producer-consumer process synchronization:

<img src="Test Images/img6.png" alt="Alt Text" width="860" height="350">

Display log text:

<img src="Test Images/img7.png" alt="Alt Text" width="860" height="350">

## Project Discussion:
Despite the challenges, the test results have been generally positive. The following aspects of the project have been tested and validated:

1. Process Creation: The creation of new processes was tested, and the logs confirmed the successful launch of these processes.

2. Thread Creation: Threads were created within processes, and their behavior was observed. The log entries confirmed that threads were created and executed as expected.

3. Process and Thread Termination: Processes and threads were successfully terminated upon user command. The termination of processes and threads was confirmed through log entries.

4. IPC Message Handling: Inter-Process Communication (IPC) messages were sent and received correctly between processes. The logs provided a record of sent and received messages.

5. Process Synchronization: Process synchronization was tested using producer-consumer scenarios, and the logs confirmed the correct synchronization of threads.

6. Log File Management: The project's ability to create and manage log files was tested. Log files were successfully created, and their content was displayed as expected.
