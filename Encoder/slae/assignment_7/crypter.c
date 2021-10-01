#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FIRST_BYTE 1
#define CHARACTER_SET_SIZE 255

int encrypt(int characterSet[][CHARACTER_SET_SIZE], unsigned char *key, unsigned char *payload, short debug)
{
    int payloadLength = strlen((char *)payload);

    // Loop through each char in payload, and use the values from
    // the corresponding char from the key to determine which byte
    // to select from characterSet and use it as the encoded byte.
    int encrypted[payloadLength];
    for (int i = 0; i < payloadLength; i++)
    {
        int currentByte = (int)payload[i];
        int keyByte = (int)key[i];
        encrypted[i] = characterSet[keyByte - FIRST_BYTE][currentByte - FIRST_BYTE];

        if (debug)
        {
            printf("Position: %d\n", i);
            printf("Payload byte (dec): %d\n", (int)payload[i]);
            printf("Key byte (dec): %d\n", keyByte);
            printf("Encrypted byte (dec): %d\n\n", encrypted[i]);
        }
    }

    printf("\nEncrypted: ");
    for (int i = 0; i < payloadLength; i++)
    {
        printf("\\x%02x", (int)encrypted[i]);
    }

    printf("\n");

    return 0;
}

int decrypt(int characterSet[][CHARACTER_SET_SIZE], unsigned char *key, unsigned char *ciphertext, short execute, short debug)
{
    int payloadLength = strlen((char *)ciphertext);
    unsigned char originalPayload[payloadLength];

    for (int i = 0; i < payloadLength; i++)
    {
        int encryptedByte = (int)ciphertext[i];
        int keyByte = (int)key[i];

        for (int i2 = 0; i2 < CHARACTER_SET_SIZE; i2++)
        {
            if (characterSet[keyByte - FIRST_BYTE][i2] == encryptedByte)
            {
                if (debug)
                {
                    printf("Position: %d\n", i);
                    printf("Payload byte (dec): %d\n", (int)ciphertext[i]);
                    printf("Key byte (dec): %d\n", keyByte);
                    printf("Decrypted byte (dec): %d\n\n", characterSet[0][i2]);
                }

                originalPayload[i] = (unsigned char)characterSet[0][i2];
                break;
            }
        }
    }

    if (execute == 1)
    {
        void (*s)() = (void *)originalPayload;
        s();
    }
    else
    {
        printf("\nDecrypted: ");
        for (int i = 0; i < payloadLength; i++)
        {
            printf("\\x%02x", (int)originalPayload[i]);
        }

        printf("\n");
    }

    return 0;
}

unsigned char* parseByteString(char *byteString)
{
    unsigned int byteStringLength = strlen(byteString);
    char byteStringCopy[byteStringLength];
    strcpy(byteStringCopy, byteString);

    unsigned int length = 0;
    for (unsigned int i = 0; i < byteStringLength; i++)
    {
        if (byteStringCopy[i] == 'x')
        {
            length += 1;
        }
    }

    unsigned char* parsedString = (unsigned char*)malloc(sizeof (unsigned char) * length);
    const char delim[3] = "\\x";
    char *b;

    b = strtok(byteStringCopy, delim);
    int currentByte = 0;

    while( b != NULL ) {
        char parsedByte = (char)(int)strtol(b, NULL, 16);
        parsedString[currentByte] = parsedByte;
        currentByte += 1;
        b = strtok(NULL, delim);
    }

    return parsedString;
}

int main(int argc, char **argv)
{
    short debug = argc == 5;
    int characterSet[CHARACTER_SET_SIZE][CHARACTER_SET_SIZE];

    // Loop for each permutation required
    for (int i = 0; i < CHARACTER_SET_SIZE; i++)
    {
        // Add each character to the right of the
        // initial offset to the start of the row.
        for (int i2 = i; i2 < CHARACTER_SET_SIZE; i2++)
        {
            characterSet[i][i2 - i] = i2 + FIRST_BYTE;
        }

        // Rotate the characters to the left of the
        // initial offset to the end of the row.
        for (int i2 = 0; i2 < i; i2++)
        {
            characterSet[i][(CHARACTER_SET_SIZE - i) + i2] = i2 + FIRST_BYTE;
        }
    }

    char *mode = argv[1];

    unsigned char *baseKey = parseByteString(argv[2]);
    int keyLength = strlen((char *)baseKey);

    if (debug)
    {
        printf("Key: ");

        for (unsigned int i = 0; i < strlen((char *)baseKey); i++)
        {
            printf("%02x ", baseKey[i]);
        }

        printf("\n");
    }


    unsigned char *payload = parseByteString(argv[3]);
    int payloadLength = strlen((char *)payload);

    if (debug)
    {
        printf("Payload: ");

        for (unsigned int i = 0; i < strlen((char *)payload); i++)
        {
            printf("%02x ", payload[i]);
        }

        printf("\n");
    }


    int inflatedKeySize = keyLength;
    int iterationsNeeded = 1;

    // If the payload is larger than the key, the key needs to be
    // repeated N times to make it match or exceed the length of
    // the payload.
    if (payloadLength > keyLength)
    {
        // Determine the number of times the key needs to be expanded
        // to meet the length required to encrypt the payload.
        iterationsNeeded = (int)((payloadLength / keyLength) + 0.5) + 1;

        // Determine the new key size required and store it in
        // inflatedKeySize for use when initialising the new key.
        inflatedKeySize = keyLength * iterationsNeeded;
    }

    // Initialise the key with a null byte so that strcat can work.
    unsigned char key[inflatedKeySize];
    key[0] = '\x00';

    // Concatenate the base key on to the new key to ensure it
    // is long enough to encrypt the payload.
    for (int i = 0; i < iterationsNeeded; i++)
    {
        strcat((char *)key, (char *)baseKey);
    }

    if (strcmp(mode, "e") == 0)
    {
        return encrypt(characterSet, key, payload, debug);
    }

    if (strcmp(mode, "d") == 0)
    {
        return decrypt(characterSet, key, payload, 0, debug);
    }

    if (strcmp(mode, "x") == 0)
    {
        return decrypt(characterSet, key, payload, 1, debug);
    }

    return 0;
}
