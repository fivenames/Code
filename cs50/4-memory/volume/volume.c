// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

//FILE is a type declared in C std lib. A variable of type FILE is created when a file is opened.
//The "input" is the memory address of the FILE type, returned by the function fopen().
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

//The fopen() function creates the file if it does not exist.
    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    //unsigned int of 8 bits/ 1 bytes. Equals to the size of each header in WAV file type.
    uint8_t header[HEADER_SIZE];

//The opened file “remembers” the number of bytes that were successfully read, hence subsequent calls to this function for the same file will return bytes after those already read.
//1. ptr to the buffer where read memory to be stored       2. size of the type of data to read      3. Number of elements to read at once       4. ptr to the file return by fopen().
    fread(header, 1, HEADER_SIZE, input);
    fwrite(header, 1, HEADER_SIZE, output);


    //signed int of 16 bits/ 2 bytes. Equals to the size of each sample in WAV file type.
    int16_t buffer;

    //fread() returns the number of elements successfully read. All non-zero values are interpreted as true.
    //the loop will continue until the end of the file. When no more data to read, fread() will return 0 == false in boolean condition.
    while(fread(&buffer, 2, 1, input))
    {
        //update the buffer, scalling the volume
        buffer *= factor;
        fwrite(&buffer, 2, 1, output);
    }

    fclose(input);
    fclose(output);
}
