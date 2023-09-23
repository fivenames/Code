#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<cs50.h>
// argc: argument count = number of words in the command line,      argv: argument vector = array of words in the command line
int main (int argc, string argv[])
{
    //check whether argv[1] is in existence or not first.
    if(argc != 2)
    {
        printf("./caesar key\n");
        return 1;
    }

    for(int i = 0; i < strlen(argv[1]); i++)
    {
        //function returns 0 if input is not a number.
        if(isdigit(argv[1][i]) == 0)
        {
            printf("./caesar key\n");
            return 2;
        }
    }

    int key = atoi(argv[1]);

    string plain = get_string("Plaintext: ");

    string cipher = plain;

    for(int i = 0; i < strlen(plain); i++)
    {
        if(isalpha(plain[i]))
        {
            if(isupper(plain[i]))
            {
                //convert ascii value to alphabetical value starting at 0, shift the value using the formula, convert back to ascii value.
                cipher[i] = (((plain[i] - 65) + key) % 26) + 65;
            }
            else
            {
                cipher[i] = (((plain[i] - 97) + key) % 26) + 97;
            }
        }
    }

    printf("%s\n", cipher);
}