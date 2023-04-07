#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header)
{
    // 1. 87 == "W" ASCII value     2. 0x41 == 65 == "A"     3. 0b1010110 == 86 == "V"    4. 69 == "E"
    if(header.format[0] == 87 && header.format[1] == 0x41 && header.format[2] == 0b1010110 && header.format[3] == 69)
    {
        return 0;
    }
    else
    {
        return 5;
    }
}

// Return an integer representing the block size of the given WAV file, in bytes.
int get_block_size(WAVHEADER header)
{
    int block_size = header.numChannels * (header.bitsPerSample / 8);

    return block_size;
}


int main(int argc, char *argv[])
{
    // Ensure proper usage
    if(argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    // Open input file for reading
    FILE *infile = fopen(argv[1], "r");
    if(infile == NULL)
    {
        printf("Could not open %s\n", argv[1]);
        return 2;
    }

    // Read header into an array
    WAVHEADER header[1];

    fread(header, 44, 1, infile);

    // Use check_format to ensure WAV format
    if(check_format(header[0]) != 0)
    {
        printf("Invalid input file, input WAV file.\n");
        return 3;
    }

    // Open output file for writing
    FILE *outfile = fopen(argv[2], "w");
    if(outfile == NULL)
    {
        printf("Could not create %s\n", argv[2]);
        return 4;
    }

    // Write header to file
    fwrite(header, 44, 1, outfile);

    // Use get_block_size to calculate size of block
    int block_size = get_block_size(header[0]);

    // Write reversed audio to file
/*
The fseek() function sets the file position indicator for the stream.
1. pointer to the opened file    2. bytes to offset    3. SEEK_SET, SEEK_CUR, SEEK_END - the offset relative to the start-of-file, the current position indicator, or end-of-file.
*/
    fseek(infile, -(block_size), SEEK_END);

    uint8_t buffer[block_size];

// The ftell function in C returns the value of current file position of a stream in an open file, measured in bytes, from the beginning of the file.
// Loop stops at offset 43 bytes is because when fseek first points at bytes 44, there is still audio unread and unwritten.
    while(ftell(infile) > 43)
    {
        fread(buffer, block_size, 1, infile);
        fwrite(buffer, block_size, 1, outfile);

        fseek(infile, -(2 * block_size), SEEK_CUR);
    }

    fclose(infile);
    fclose(outfile);

    return 0;
}