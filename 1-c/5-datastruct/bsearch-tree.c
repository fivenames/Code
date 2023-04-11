#include<stdio.h>
#include<stdlib.h>

/*
consider: 1, 2, 3, 4, 5, 6, 7

Binary search, take the middle number: 4
left half: 2
right half: 6

making the 7 numbers into a binary search tree, they can be linked as follows:

            4
         2     6
        1 3   5 7
*/


typedef struct node
{
    int data;
    struct node *left_node;
    struct node *right_node;
}
node;

node *tree;

int main()
{
    tree = NULL;
    return 0;
}