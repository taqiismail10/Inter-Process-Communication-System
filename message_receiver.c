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

// Function to receive messages from the queue
void receiveMessage()
{
    // Open the message queue for receiving messages
    mqd_t mq = mq_open(QUEUE_NAME, O_CREAT | O_RDONLY, 0644, NULL);
    if (mq == (mqd_t)-1)
    {
        perror("mq_open");
        exit(1);
    }

    char buffer[MAX_SIZE + 1];

    while (1)
    {
        // Receive message from the queue
        ssize_t bytes_read = mq_receive(mq, buffer, MAX_SIZE, NULL);
        if (bytes_read >= 0)
        {
            buffer[bytes_read] = '\0'; // Null-terminate the received message
            printf("Received: %s\n", buffer);

            // Exit if the "exit" message is received
            if (strcmp(buffer, MSG_STOP) == 0)
            {
                break;
            }
        }
        else
        {
            perror("mq_receive");
            exit(1);
        }
    }

    // Close and unlink the queue
    mq_close(mq);
    mq_unlink(QUEUE_NAME);
}

int main()
{
    printf("Waiting to receive messages...\n");
    receiveMessage();
    printf("Receiver terminated.\n");

    return 0;
}
