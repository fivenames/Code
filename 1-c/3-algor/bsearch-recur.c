#include<stdio.h>
#include<stdlib.h>

int binary_search(int arr[], int size, int target)
{
    int mid_idx = (size / 2);

    if(arr[mid_idx] == target)
    {
        return 0;
    }
    else if(size < 2)
    {
        return 1;
    }

    if(target < arr[mid_idx])
    {
        int *left = malloc((mid_idx) * sizeof(int));
        if(left == NULL)
        {
            return 2;
        }

        for (int i = 0; i < mid_idx; i++)
        {
            left[i] = arr[i];
        }

        int result = binary_search(left, mid_idx, target);

        free(left);
        return result;
    }
    else if(target > arr[mid_idx])
    {
        int *right = malloc((size - (mid_idx)) * sizeof(int));
        if(right == NULL)
        {

            return 2;
        }

        for (int i = 0; i < (size - (mid_idx)); i++)
        {
            right[i] = arr[mid_idx + i];
        }

        int result = binary_search(right, size - (mid_idx), target);

        free(right);
        return result;
    }

    return 1;
}


int main(void)
{
    int size = 6, target = 0;
    printf("Target: ");
    scanf("%i", &target);

    int arr[7] = {1, 3, 4, 7, 9, 10};

    int result = binary_search(arr, size, target);

    if(result == 0)
    {
        printf("found\n");
    }
    else if(result == 2)
    {
        printf("fail to allocate memory\n");
    }
    else
    {
        printf("not found\n");
    }

    return 0;
}