#ifndef IPC_MESSAGE_QUEUE_H
#define IPC_MESSAGE_QUEUE_H

// Define constants
#define QUEUE_NAME "/my_message_queue"
#define MAX_SIZE 1024
#define MSG_STOP "exit"

// Function declarations
void sendMessage(const char *message);
void receiveMessage();

#endif // IPC_MESSAGE_QUEUE_H
