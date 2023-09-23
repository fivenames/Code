#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<cs50.h>

int main (int argc, string argv[])
{
    if(argc != 2)
    {
        printf("./substitution 'KEY'\n");
        return 1;
    }

    string key = argv[1];

    for(int i = 0; i < strlen(argv[1]); i++)
    {
        if(!isalpha(argv[1][i]) || strlen(argv[1]) != 26)
        {
            printf("Key must only contain 26 alphabetic characters.\n");
            return 2;
        }
        else
        {
            key[i] = toupper(argv[1][i]);
        }
    }

    // Create an array of 26 boolean values and initialize each element to false
    bool used_letters[26] = {false};

    // Process the key and set the corresponding element in the array to true for each letter
    for(int i = 0; i < strlen(key); i++)
    {
        // Convert the key to uppercase
        key[i] = toupper(key[i]);

        // Determine the position of the letter in the alphabet (A=0, B=1, ..., Z=25)
        int letter_pos = key[i] - 'A';

        // Set the corresponding element in the array to true
        used_letters[letter_pos] = true;
    }

    // Check whether any of the elements in the array are still false
    bool key_is_valid = true;
    for(int i = 0; i < 26; i++)
    {
        if(used_letters[i] == false)
        {
            key_is_valid = false;
            break;
        }
    }

    // If the key is invalid, print an error message and exit the program
    if(!key_is_valid)
    {
        printf("Key must not contain repeated letters of the alphabet.\n");
        return 3;
    }

    string plain = get_string("Plaintext: \n");

    string cipher = plain;

    for(int i = 0; i < strlen(plain); i++)
    {
        if(isalpha(plain[i]))
        {
            if(isupper(plain[i]))
            {
                //convert ascii value into 0 to 25, substitute using the key at that position.
                cipher[i] = key[plain[i] - 65];
            }
            else
            {
                cipher[i] = key[plain[i] - 97];
                cipher[i] = tolower(cipher[i]);
            }
        }
    }

    printf("%s\n", cipher);
}