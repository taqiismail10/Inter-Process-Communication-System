#include <fcntl.h>
#include <sys/stat.h>
#include <mqueue.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define QUEUE_NAME "/my_message_queue"
#define MAX_SIZE 1024
#define MSG_STOP "exit"

// Function to send messages to the queue
void sendMessage(const char *message)
{
    // Open the message queue for sending messages
    mqd_t mq = mq_open(QUEUE_NAME, O_CREAT | O_WRONLY, 0644, NULL);
    if (mq == (mqd_t)-1)
    {
        perror("mq_open");
        exit(1);
    }

    // Send the message to the queue
    if (mq_send(mq, message, strlen(message) + 1, 0) == -1)
    {
        perror("mq_send");
        exit(1);
    }
    printf("Sent: %s\n", message);

    // Close the queue
    mq_close(mq);
}

int main()
{
    char message[MAX_SIZE];

    printf("Enter messages to send (type 'exit' to quit):\n");

    while (1)
    {
        // Read message from user input
        printf("> ");
        fgets(message, MAX_SIZE, stdin);
        message[strlen(message) - 1] = '\0'; // Remove newline character

        // Send message
        sendMessage(message);

        // Break loop if "exit" message is sent
        if (strcmp(message, MSG_STOP) == 0)
        {
            break;
        }
    }

    return 0;
}
