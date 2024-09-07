#include <stdio.h>

void swap(int* a, int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
    
    return;
}

int partition(int* arr, int start, int end, int size){
    int pivot = arr[start]; // choose the first element as pivot
    int low = start + 1;
    int high = end;

    while(low < high){
        // increment low ptr until found an element bigger than pivot
        while(arr[low] <= pivot && low < high){
            low++;
        }
        // decrement high ptr until found an element smaller than (or equal to) pivot
        while(arr[high] > pivot && low < high){
            high--;
        }
        if(low < high){
            swap(&arr[low], &arr[high]); // swap the elements low and high ptr is pointing to, such that now the array is partitioned
        }
    }
    swap(&arr[start], &arr[low - 1]); // move the pivot to its correct position
    
    return low - 1; // return the index of the pivot
}

// quicksort algorithm
void quickSort(int* arr, int start, int end, int size){
    if(start >= end){ // if only one element in array, terminate
        return;
    }

    // partition the array such that those elements lower than the chosen pivot will always be  on the left and
    // those element higher than the pivot will be on the right of the pivot
    int idx = partition(arr, start, end, size); 
    quickSort(arr, start, idx, idx - start + 1); // recursively partition the left array and right array
    quickSort(arr, idx + 1, end, end - idx);
}

int main(){
    int size = 15;
    int arr[15] = {22, 4, 3, 52, 4, 0, 2, 9, 1, 23, 31, 53, 20, 2, 1};
    quickSort(arr, 0, size - 1, size);

    for(int i = 0; i < size; i++){
        printf("%d", arr[i]);
        printf(" ");
    }
}

/*
Time complexity:
T(n) = O(n) + T(p - 1) + T(n - p) --> n is the size of array and p is the size of the left partitioned array

Best case scenario: If p is always half of n ie. p = n / 2
    T(n) = O(n) + 2T(n / 2)
        T(n / 2) = O(n / 2) + 2T(n / 4)
    T(n) = O(n) + 2( O(n / 2) + 2T(n / 4) )
         = 2O(n) + 4T(n / 4)
    T(n) = kO(n) + 2^k T(n / 2^k)
    
    Base case: T(1) = O(1)
    when n/2^k -> 1;
        n = 2^k
        k -> log_2(n);
    T(n) = log(n)O(n) + O(1)

This is the same as merge sort


Worst case scenario: If p is 1, given a sorted array
    T(n) = O(n) + T(1) + T(n - 1)
        T(1) = O(1)
    T(n) = O(n) + T(n - 1)
        T(n - 1) = O(n - 1) + T(n - 2)
    T(n) = O(n) + O(n - 1) + O(n - 2) +...
         = O(n + (n - 1) + (n - 2) + ... + 1) = O(n^2)
*/

/*
A sorting algorithm is stable if, when two elements have the same value, their relative order is preserved in the sorted output as it was in the input. 
If two items are equal by the sorting criterion, a stable sort will not change their original order relative to each other.
*/