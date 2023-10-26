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
   - A mechanism for creating new processes, utilizing system calls such as 'fork' and 'exec'.
2. Process Management:
   - Capabilities to list, terminate, and monitor active processes.
   - Users can access information about each process, including its Process ID (PID), Parent Process ID, and state.
3. Thread Support:
   - The Process Manager can accommodate multiple threads within a process.
   - Contains means for thread creation, termination, and synchronization, leveraging system calls like 'pthread_create' and synchronization tools like mutexes and semaphores.
4. Inter-Process Communication (IPC):
   - IPC methods that facilitate communication and data sharing between processes and threads.
   - Techniques such as message passing, shared memory, and pipes for IPC, using system calls like 'pipe', 'msgget', and 'shmget'.
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
## Usage Guide:
## Test Results:
## Project Discussion:
