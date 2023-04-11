#include<stdio.h>
#include<stdlib.h>

int main()
{
/*
A queue is a type of data struct that follows the First In First Out (FIFO) principle, meaning that the first item to be added to the queue will be the first one to be removed.
A stack is a type of data struct that follows the Last In First Out (LIFO) principle, meaning that the last item to be added to the stack will be the first one to be removed.
*/
    int *arr = malloc(3 * sizeof(int));
    if(arr == NULL)
    {
        return 1;
    }

    arr[0] = 1;
    arr[1] = 2;
    arr[2] = 3;

    int *temp = malloc(4 * sizeof(int));
    if(temp == NULL)
    {
        free(arr);
        return 1;
    }

    // copying content to new allocated memory
    for(int i = 0; i < 2; i++)
    {
        arr[i] = temp[i];
    }
    temp[3] = 4;
    // free the original memory chunk.
    free(arr);
    // set arr to point to the new memory chunk.
    arr = temp;

    // reallocating memory.
/* If there is sufficent memory behind the original memory chunk, realloc will allocate the memory behind the memory chunk without finding a new memory chunk.
 Declaring temp pointer so to prevent memory leak in the event that realloc fails and return NULL, it will overwrite the arr pointer if temp is undeclared. Old memory chunk is lost.*/
    int *temp = reaclloc(arr, 5 * sizeof(int));
    if(temp == NULL)
    {
        free(arr);
        return 1;
    }
    temp[4] = 5;
    // free is not needed as realooc auto free the original memory.
    // copying is not needed as realloc auto does it.
    arr = temp;

// Adding elements to an array will always result in a need to copy the whole array into a new allocated memory chunk. However, a linked list can do something different.
}

/*
note:

----------
|  heap  |
|        |
|        |
|        |
|  stack |
----------

malloc() will allocate memory from the heap down, where functions will create stack frames up when called.
Hence when function call returns, the memory allocated by malloc() will not be affected.
*/