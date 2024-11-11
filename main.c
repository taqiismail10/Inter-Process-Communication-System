#include "ipc_message_queue.h"
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s [sender|receiver]\n", argv[0]);
        return 1;
    }

    if (strcmp(argv[1], "sender") == 0)
    {
        char message[MAX_SIZE];
        printf("Enter messages to send (type 'exit' to quit):\n");

        while (1)
        {
            printf("> ");
            fgets(message, MAX_SIZE, stdin);
            message[strlen(message) - 1] = '\0'; // Remove newline character

            sendMessage(message);

            if (strcmp(message, MSG_STOP) == 0)
            {
                break;
            }
        }
    }
    else if (strcmp(argv[1], "receiver") == 0)
    {
        printf("Waiting to receive messages...\n");
        receiveMessage();
        printf("Receiver terminated.\n");
    }
    else
    {
        printf("Invalid argument. Use 'sender' or 'receiver'.\n");
        return 1;
    }

    return 0;
}
