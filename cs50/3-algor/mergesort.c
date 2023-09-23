#include <stdio.h>
#include <stdlib.h>

// Note: the function merge_sort the line *merge(arr, left, mid, right, size - mid);* passed the value of left_size and right_size as mid and size-mid respectively.
// Hence it is not necessary to intialise the value of left_size and right_size.
void merge(int * arr, int * left, int left_size, int * right, int right_size)
{
    int i = 0, j = 0, k = 0;

    // Compare elements of left and right arrays and
    // store the smaller element in the original array
    while (i < left_size && j < right_size)
    {
        if (left[i] < right[j])
        {
            //equivalent to
            //arr[k] = left[i];
            //k++;
            //j++;
            arr[k++] = left[i++];
        }
        else
        {
            //note that ++ operator is post-increment operators, meaning it increase the value of the int after the assignment has been performed.
            arr[k++] = right[j++];
        }
    }

    // If there are any remaining elements in the left array (left array has one number more than right array), append them to the original array.
    while (i < left_size)
    {
        arr[k++] = left[i++];
    }

    while (j < right_size)
    {
        arr[k++] = right[j++];
    }
}

void merge_sort(int * arr, int size)
{
    // Base case: if the array has less than 2 elements, it is already sorted
    if (size < 2)
    {
        return;
    }

    // Split the array into two halves
    int mid = size / 2;
    //The malloc() function takes one argument: number of bytes of memory to allocate. It returns a pointer to the start of the allocated memory, or 'NULL' if allocation fails.
    //The sizeof() operator returns in bytes, the size of a variable.
    
//It is used to determine how much memory an int variable occupies - may be different on different machines, depending on the architecture and the implementation of the C compiler.
    int * left = malloc(mid * sizeof(int));
    //In case that size of the arr is odd number, use size - mid will place the extra one int at the right half.
    int * right = malloc((size - mid) * sizeof(int));

    for (int i = 0; i < mid; i++)
    {
        left[i] = arr[i];
    }

    for (int i = 0; i < size - mid; i++)
    {
        right[i] = arr[mid + i];
    }

    // Recursively sort the two halves
/*
In this case, **left array pass in as the whole array**, and mid becomes the length of array, each stack frame called the value of left and mid will be updated,
so the array will be further split until there is only one int inside it - it is considered sorted.
*/
    merge_sort(left, mid);

    merge_sort(right, size - mid);

    // Merge the 'sorted' halves, this function is first called after the final stack frame, so it is first executed on 2 arrays of single element, increasing the array size each call.
/*
Note: at different level of stack frames, the arr varaible takes on different set of data, **at 1 frame higher, its arr is equal to the left||right array of a frame lower**.
Hence after the higher frame is poped, the left array of the current frame is sorted, the function is then recursively called to sort the left and the right array on current frame,
which then becomes the left||right array of the lower frame
*/
    merge(arr, left, mid, right, size - mid);

    // Impt to free the memory after using malloc function, allowing it to be reused after each stack frame. Failing to do this can lead to memory leaks and other issues.
    free(left);
    free(right);
}

int main()
{
    int arr[] = {5, 2, 4, 7, 1, 3, 2, 6};
    //the size of the whole array in bytes divide by the size of a single integer in the array in bytes = the number of integer in the array.
    int size = sizeof(arr) / sizeof(arr[0]);

    merge_sort(arr, size);

    for (int i = 0; i < size; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
