#include <stdio.h>

void bubble_sort(int arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        //from arr[0] swap place with next arr if the latter is smaller
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                // Swap arr[j] and arr[j+1]
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
/*
If you define and use a function swap(), int has to be passed to the function as memory address to ensure that the change is also made in the memory of main().
Function uses different part of the memory, called the memory stack, the memory will be on top of the main().
If an int is passed, the function creates the values at another memory location and execute without touching the main()'s part of memory.
*/
            }
        }
        //repeat the cycle from arr[0] till arr[n - 2] as the arr[n - 1], the last number in the arr, will already be the largest.
    }
}

int main() {

    int n;
    printf("The number of int: ");
    scanf("%i", &n);

    int arr[n];
    printf("Int to sort: \n");
    for(int i = 0; i < n; i++)
    {
        scanf("%i", &arr[i]);
    }

    bubble_sort(arr, n);

    // Print the sorted array
    for (int i = 0; i < n; i++)
    {
        printf("%i ", arr[i]);
    }
    printf("\n");

    return 0;
}
