#include <stdio.h>
#include <stdlib.h>

int main(void){
    int (*ptr)[5]; // delcares a pointer that points to the type int fixed array of 5 elements.
    // Note this is different from int *ptr[5], which denotes an array of type int pointers.
    
    ptr = calloc(3, sizeof(int[5])); // dynamic allocate memory.

    printf("%i", ptr[1][4]);
    return 0;
}
// fixed size of 2D array use: int[][];
// fixed size array of dynamic size of arrays use: int *[]; (row number fixed)
// dynamic size of array of fixed size arrays use: int (*)[]; (column number fixed)
// dynamic size of 2D array use: int **ptr;