// Saves popular dog names in a trie

/*
Trie is implemented using a combination of linked list and array.
Tri is a linked list of arrays of nodes.
Example, 5 arrays of 26 alphabets link by linked list, to store Harry's data, H-A-R-R-Y, such that each letter is a node in the array that points to the next node in the next array.

Tri has a runtime of O(1) as the size of data, n, does not affect the number of steps to take to find the target.
*/

#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE_OF_ALPHABET 26
#define MAXCHAR 20

typedef struct node
{
    bool is_word;
    struct node *children[SIZE_OF_ALPHABET];
}
node;

// Function prototypes
bool check(char *word);
bool unload(void);
void unloader(node *current);

// Root of trie, a pointer that points to the node at the beginning of the link list.
node *root;

// Buffer to read dog names into
char name[MAXCHAR];

int main(int argc, char *argv[])
{
    // Check for command line args
    if (argc != 2)
    {
        printf("Usage: ./trie infile\n");
        return 1;
    }

    // File with names
    FILE *infile = fopen(argv[1], "r");
    if (!infile)
    {
        printf("Error opening file!\n");
        return 1;
    }

    // Allocate root of trie
    root = malloc(sizeof(node));

    if (root == NULL)
    {
        return 1;
    }

    root->is_word = false;
    for (int i = 0; i < SIZE_OF_ALPHABET; i++)
    {
        root->children[i] = NULL;
    }

    // Add words to the trie
    while (fscanf(infile, "%s", name) == 1)
    {
        node *cursor = root;

        // Iterate each of the char thru the name.
        for (int i = 0, n = strlen(name); i < n; i++)
        {
            // get the idx of the char
            int index = tolower(name[i]) - 'a';

            // if the array within the node do not contain the letter
            if (cursor->children[index] == NULL)
            {
                // Make node
                node *new = malloc(sizeof(node));
                new->is_word = false;
                for (int j = 0; j < SIZE_OF_ALPHABET; j++)
                {
                    new->children[j] = NULL;
                }
                // set the cursor to point at the next node.
                cursor->children[index] = new;
            }

            // If this particular node alr contains the letter. Go to node that have been made.
            cursor = cursor->children[index];
        }

        // if we are at the end of the word, mark it as being a word
        cursor->is_word = true;
    }

    if (check(get_string("Check word: ")))
    {
        printf("Found!\n");
    }
    else
    {
        printf("Not Found.\n");
    }

    if (!unload())
    {
        printf("Problem freeing memory!\n");
        return 1;
    }

    fclose(infile);
}

// Return true if found, false if not found.
bool check(char* word)
{
    node *ptr = root;

    for(int i = 0, n = strlen(word); i < n; i++)
    {
        int idx = tolower(word[i]) - 'a';

        if (ptr -> children[idx] == NULL)
        {
            return false;
        }
        else
        {
            ptr = ptr -> children[idx];
        }
    }

    if(ptr -> is_word == true)
    {
        return true;
    }

    return false;
}

// Unload trie from memory
bool unload(void)
{

    // The recursive function handles all of the freeing
    unloader(root);

    return true;
}

void unloader(node* current)
{

    // Iterate over all the children to see if they point to anything and go there if they do point
    for (int i = 0; i < SIZE_OF_ALPHABET; i++)
    {
        if (current->children[i] != NULL)
        {
            unloader(current->children[i]);
        }
    }

    // After we check all the children point to null we can get rid of the node and return to the previous iteration of this function.
    free(current);
}
