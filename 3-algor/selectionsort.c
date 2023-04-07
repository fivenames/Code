#include<stdio.h>

void selection_sort(int arr[], int n)
{
    int min_idx;

    for(int i = 0; i < n - 1; i++)
    {
        //intialise the minimum number to be arr[i]
        min_idx = i;
        for(int j = i + 1; j < n; j++)
        {
            //from arr[1], compare subsequent number, if smaller, replace with new index
            if(arr[j] < arr[min_idx])
            {
                min_idx = j;
            }
        }
        //replace arr[0] with smallest number and loop agn starting with arr[1]
        int temp = arr[i];
        arr[i] = arr[min_idx];
        arr[min_idx] = temp;
    }
}

int main()
{
    int n;
    printf("How many int: ");
    scanf("%d", &n);

    int arr[n];
    printf("Int: \n");
    for(int i = 0; i < n; i++)
    {
    scanf("%d", &arr[i]);
    }

    selection_sort(arr, n);

    for (int i = 0; i < n; i++)
    {
        printf("%i ", arr[i]);
    }
    printf("\n");

    return 0;
}