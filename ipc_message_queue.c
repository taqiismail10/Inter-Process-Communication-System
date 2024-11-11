#include "ipc_message_queue.h"
#include <fcntl.h>
#include <sys/stat.h>
#include <mqueue.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Function to send messages to the queue
void sendMessage(const char *message)
{
    mqd_t mq = mq_open(QUEUE_NAME, O_CREAT | O_WRONLY, 0644, NULL);
    if (mq == (mqd_t)-1)
    {
        perror("mq_open");
        exit(1);
    }

    if (mq_send(mq, message, strlen(message) + 1, 0) == -1)
    {
        perror("mq_send");
        exit(1);
    }
    printf("Sent: %s\n", message);

    mq_close(mq);
}

// Function to receive messages from the queue
void receiveMessage()
{
    mqd_t mq = mq_open(QUEUE_NAME, O_CREAT | O_RDONLY, 0644, NULL);
    if (mq == (mqd_t)-1)
    {
        perror("mq_open");
        exit(1);
    }

    // Get message queue attributes to determine max message size
    struct mq_attr attr;
    if (mq_getattr(mq, &attr) == -1)
    {
        perror("mq_getattr");
        exit(1);
    }

    char *buffer = (char *)malloc(attr.mq_msgsize);
    if (buffer == NULL)
    {
        perror("malloc");
        exit(1);
    }

    while (1)
    {
        ssize_t bytes_read = mq_receive(mq, buffer, attr.mq_msgsize, NULL);
        if (bytes_read >= 0)
        {
            buffer[bytes_read] = '\0';
            printf("Received: %s\n", buffer);

            if (strcmp(buffer, MSG_STOP) == 0)
            {
                break;
            }
        }
        else
        {
            perror("mq_receive");
            free(buffer);
            exit(1);
        }
    }

    free(buffer);
    mq_close(mq);
    mq_unlink(QUEUE_NAME);
}
