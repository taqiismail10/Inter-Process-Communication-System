# Inter-Process Communication System (IPC)

## Project Structure
 ───Interprocess Communication System  
    ├── ipc_message_queue.c  
    ├── ipc_message_queue.h  
    ├── ipc_project  
    ├── main.c  
    ├── message_receiver.c  
    ├── message_sender.c  
    └── README.md  
## Files and Components

- **ipc_message_queue.h**: Contains the constant definitions and functionsfor the message-passing mechanism.
- **ipc_message_queue.c**: Implements the `sendMessage` and `receiveMessage` functions using POSIX message queues.
- **main.c**: Main program entry point, with command-line arguments to run either the sender or receiver.
- **message_sender.c**: Implements the sender logic, which takes user input messages and sends them to the queue.
- **message_receiver.c**: Implements the receiver logic, which reads messages from the queue.

## Compilation
Navigate to the project directory and compile the program using GCC with the following command:
```bash
gcc -o ipc_project main.c ipc_message_queue.c -lrt
```
### Running the Programs
Open two terminal windows.
1. In the first terminal, start the receiver process:
```bash
./ipc__project receiver
```
2. In the second terminal, start the sender process:
```bash
./ipc_project sender
```
### Sample Output
`Sender Terminal`
```bash
Enter messages to send (type 'exit' to quit):
> Hello from the sender!
Sent: Hello from the sender!
> exit
Sent: exit
```
`Receiver Terminal`
```bash
Waiting to receive messages...
Received: Hello from the sender!
Received: exit
Receiver terminated.
```

## Conclusion

This IPC system provides a simple and educational example of message passing using POSIX message queues in a Linux environment. The setup demonstrates the fundamentals of asynchronous communication between processes and the advantages of using a loosely coupled system.

Additionally, the project will be extended to implement several more advanced IPC techniques:

- **Shared Memory**: The system will implement a shared memory approach, allowing multiple processes to read from and write to a common memory segment. This feature will emphasize the high-speed nature of shared memory-based communication and its implications on synchronization.
  
- **Semaphores and Synchronization**: Semaphores will be employed to handle synchronization issues in shared memory and message-passing systems. It will include scenarios demonstrating how semaphores can prevent race conditions and ensure mutual exclusion, which are crucial for maintaining data consistency in concurrent environments.
  
- **Pipes**: The system will utilize pipes to demonstrate one-way and two-way communication between processes. Pipes provide an easy and efficient way for processes to exchange data, and this feature will illustrate their usefulness for simpler inter-process communication scenarios.
  
- **Graphical Representation**: To enhance user comprehension, the system will provide visual feedback on communication flows, synchronization statuses, and message-passing operations. This will offer users an intuitive understanding of how the processes communicate, synchronize, and share data.

These features will collectively enhance the system's robustness, providing a comprehensive and practical learning experience in IPC and process synchronization.
