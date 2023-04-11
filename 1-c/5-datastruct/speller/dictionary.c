// Implements a dictionary's functionality

/*
Hash table implemented through a combination of array and linked list.
It can sort linked lists into an array. Example like the contacts in the phone, where the contacts are sorted alphabetically.

Hash table can theoritically achieve O(1) runtime as every input can direct straight to an idx of the array which points to the node.
Strictly speaking, the runtime is O(n), but increasing the size of the array (k) will make it closer to O(1). Can be viewd as O(n/k), only when k > n, runtime is O(1).
Example input of a name "John", a hash function can be written to return "10", the idx of J in alphabet.
*/

#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// An array of pointers that points to node data type.
node *table[N];



// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    node *ptr = table[hash(word)];

    while(ptr != NULL)
    {
// Before calling strcasecmp, a check on ptr for NULL is must, because if there is mispelled word, the word will not be present on the hash table.
// The function called will try to access memory that it is not supposed to be accessed, which can result in a segmentation fault.
        if(strcasecmp(word, ptr -> word) == 0)
            {
                return true;
            }

        ptr = ptr -> next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary, unsigned int *numberofwords)
{
    FILE *dict = fopen(dictionary, "r");
    if(dictionary == NULL)
    {
        printf("Failed to open dictionary\n");
        return false;
    }

    for(int i = 0; i < 26; i++)
    {
        table[i] = NULL;
    }

    unsigned int counter = 0;
    char string[LENGTH + 1];
    //fscanf() returns EOF(end-of-file), once reaches the end of file
    while(fscanf(dict, "%s", string) != EOF)
    {
        node *temp = malloc(sizeof(node));
        if(temp == NULL)
        {
            printf("Failed to allocate memory\n");
            return false;
        }

        unsigned int i = hash(string);

        strcpy(temp -> word, string);
        temp -> next = table[i];

        table[i] = temp;

        counter++;
    }

    // To "return" multiple value, pass the function an address of a data in main, alter the data by dereferencing in the function.
    *numberofwords = counter;
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(unsigned int numberofwords)
{
    return numberofwords;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for(int i = 0; i < 26; i++)
    {
        node *ptr = table[i];

        while(ptr != NULL)
        {
            node *temp = ptr -> next;
            free(ptr);
            ptr = temp;
        }
    }

    return true;
}
