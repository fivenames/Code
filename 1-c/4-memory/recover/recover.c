#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    while(argc != 2)
    {
        printf("Usage: ./recover filepath\n");
        return 1;
    }

    FILE *infile = fopen(argv[1], "r");
    if(infile == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 2;
    }

/*
Recall that 1 byte is 8-bits which is eight '0's and '1's in binary, it can be interpreted as a value.
All data of all files are stored in the computer's memory in binary, the way the computer interprets and displays the data depends on the file format.
However, other representation can be used, such as decimal, hex, octal, etc. This is a way of visualising the binary data, and the computer will  "understand".
*/
    //defines a new type called BYTE to be a uint8_t (a type defined in stdint.h, representing an 8-bit unsigned integer).
    typedef uint8_t BYTE;
    BYTE buffer[512];

// Declaring outside the loop so that free and fclose can be used after the loop ended.
    FILE *outfile;
    char *filename = malloc(8);

    while(fread(buffer, 1, 512, infile))
    {
        // Method of bitwise arithmetic.
/*
'0xf0' is a hexadecimal constant that can be represented as binary as '0b11110000' and '&' is the bitwise AND operator.
A bitwise AND operation takes two binary values (in this case buffer[3] and 'ob11110000') and returns 1 if both input bits are 1, and returns 0 otherwise.
Hence if buffer[3] has a value of 0xe(1 to f), meaning '0b1110(xxxx)', the resulting new binary value of the AND operation will be '0b11100000' == '0xe0'.
This operation will result in the lower 4 bits to be all 0 and the higher 4 bits dependent on buffer[3]. Basically solely looking at the first 4 bits of buffer[3], is it 0xe().
*/
        if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            int counter = 1;

            //this function print, not to the screen, but to a string.
// 3 parameter:     1. the name of the string to print to     2. the format of the string that is going to be print     3. the number to substitute.
// '%3i' meaning an int with 3 digits. Numbers do not require 3 digit will still be in 3 digits, such as '001'.
            sprintf(filename, "%03i.jpg", counter);

            outfile = fopen(filename, "w");
            if(infile == NULL)
            {
                 printf("Could not create %s.\n", filename);
                         return 3;
            }

            fwrite(buffer, 1, 512, outfile);

            while(fread(buffer, 1, 512, infile))
            {
                if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
                {
                    fclose(outfile);
                    counter++;
                    sprintf(filename, "%03i.jpg", counter);

                    outfile = fopen(filename, "w");
                    if(infile == NULL)
                    {
                        printf("Could not create %s.\n", filename);
                         return 3;
                    }

                    fwrite(buffer, 1, 512, outfile);
                }
                else
                {
                    fwrite(buffer, 1, 512, outfile);
                }
            }

        }
        else
        {
            continue;
        }
    }

    fclose(infile);
    fclose(outfile);
    free(filename);

    return 0;
}