#include<stdio.h>
#include<stdlib.h>

/*
Creating a linked list can link data what are stored in a non-contiguous manner.
Node is an element in a linked list. A node in a linked list typically consists of two parts: data and a pointer to the next node in the list.

     typedef struct;
     {
        int data;
        node *next_node;
     }
     node;

'typedef' keyword is used to create an alias for an existing data type, while the 'struct' keyword is used to define a newly defined data type.
However, this code will not compile as the node is defined after the data struct, the node inside the data struct is undefined.
*/

typedef struct node
{
    int data;
    // a pointer that points a node data type;
    struct node *next_node;
}
node;

// Linked lists are faster than using realloc() when adding data to a list as the step of copying is not needed. However, more memory is needed and data in the list cannot be indexd.

// A singly linked list such that the programme can only read in one direction. (A doubly linked list can also be implemented to allow the programme to move back-and-forth)
int main()
{
    // Linked list of a stack.
    node *stack = NULL;

    node *temp = malloc(sizeof(node));
    if(temp == NULL)
    {
        return 1;
    }

    // Going to the address of the node and step into the data struct to assign data to be 1.
// This is equivalent to temp -> number = 1; This syntax is used for linked lists.
    (*temp).data = 1;
    temp -> next_node = NULL;

    stack = temp;

    temp = malloc(sizeof(node));
    if(temp == NULL)
    {
        return 1;
    }

    temp -> data = 2;
    temp -> next_node = stack;
    // node 2 points to node 1.

    stack = temp;

    temp = malloc(sizeof(node));
    if(temp == NULL)
    {
        return 1;
    }

    temp -> data = 3;
    temp -> next_node = stack;

    stack = temp;

    // print out the linked list.
    node *ptr = stack;

    while(ptr != NULL)
    {
        printf("%i\n", ptr -> data);
        // replace ptr with the next node address.
        ptr = ptr -> next_node;
    }

    ptr = stack;

    while(ptr != NULL)
    {
        // declare temp pointer to store the next memory address as once memory freed, the address contained in the node is gone.
        node *next = ptr -> next_node;
        free(ptr);
        ptr = next;
    }


    // Linked list of a queue.
    node *queue = NULL;

    temp = malloc(sizeof(node));
    if(temp == NULL)
    {
        return 1;
    }

    temp -> data = 1;
    queue = temp;
    temp -> next_node = NULL;

    temp = malloc(sizeof(node));
    if(temp == NULL)
    {
        return 1;
    }

    temp -> data = 2;
    queue -> next_node = temp;
    temp -> next_node = NULL;

    ptr = queue;

    while(ptr != NULL)
    {
        printf("%i\n", ptr -> data);
        ptr = ptr -> next_node;
    }

    ptr = queue;

    while(ptr != NULL)
    {
        node *next = ptr -> next_node;
        free(ptr);
        ptr = next;
    }

    return 0;
}
