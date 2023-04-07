#include <stdio.h>

int binary_search(int arr[], int size, int target)
{
    //lower bound is the idx of the lower bound set to the array.
    int lower_bound = 0, higher_bound = (size - 1);
    while (lower_bound <= higher_bound)
    {
        int mid = (lower_bound + higher_bound) / 2;
        if (arr[mid] == target)
        {
            return mid;
        }
        else if (target > arr[mid])
        {
            // +1 or -1 is necessary as the target isn't at the mid idx. Without updating the boundary accurately, the loop will continue forever. ie;
            // taking the mid idx of the last and second last idx will always round back to the second last.
            lower_bound = mid + 1;
        }
        else
        {
            higher_bound = mid - 1;
        }
    }
    return -1;
}

int main(void)
{
    int size = 7;
    int target = 0;
    printf("Target: ");
    scanf("%i", &target);

    int arr[7] = {1, 3, 4, 7, 9, 10, 16};

    int result = binary_search(arr, size, target);

    if(result != -1)
    {
        printf("found\n");
    }
    else
    {
        printf("not found\n");
    }

    return 0;
}
