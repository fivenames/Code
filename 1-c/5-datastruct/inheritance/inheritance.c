// Simulate genetic inheritance of blood type

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Each person has two parents and two alleles
typedef struct person
{
    struct person *parents[2];
    char alleles[2];
}
person;

const int GENERATIONS = 3;
const int INDENT_LENGTH = 4;

person *create_family(int generations);
void print_family(person *p, int generation);
void free_family(person *p);
char random_allele();

int main(void)
{
    // Seed random number generator
    srand(time(0));

    // Create a new family with three generations
    person *p = create_family(GENERATIONS);

    // Print family tree of blood types
    print_family(p, 0);

    // Free memory
    free_family(p);
}

// Create a new individual with `generations`
person *create_family(int generations)
{
    person *ptr = malloc(sizeof(person));

    // If there are still generations left to create
    if (generations > 1)
    {
        // Create two new parents for current person by recursively calling create_family,
        // when called, parent0 is allocated memory, and a newset of 'parent0' & 'parent1' is also created by recursion, same for the parent1 here.
/*
Note: as recursion works on the basis of call stack: a new stack frame is created for each recursive call, new stack frame is added to the top of the stack.
A stack frame is a region of memory used to store the local variables, function arguments, and return address for a function call.
Once the top frame has excuted completely, ie. the memory address is stored and linked in the data struct, the layer will be poped.
Hence the same named variable can the take up a new set of local data and execute each of the stack frame, until the base condition is met.
*/
        person *parent0 = create_family(generations - 1);
        person *parent1 = create_family(generations - 1);

        ptr->parents[0] = parent0;
        ptr->parents[1] = parent1;

        int r = rand() % 2;
        if (r == 0)
        {
            ptr->alleles[0] = parent0->alleles[0];
        }
        else
        {
            ptr->alleles[0] = parent0->alleles[1];
        }
        r = rand() % 2;
        if (r == 0)
        {
            ptr->alleles[1] = parent1->alleles[0];
        }
        else
        {
            ptr->alleles[1] = parent1->alleles[1];
        }
    }

    // If there are no generations left to create
    else
    {
        ptr->parents[0] = NULL;
        ptr->parents[1] = NULL;

        ptr->alleles[0] = random_allele();
        ptr->alleles[1] = random_allele();
    }

    return ptr;
}

// Free `p` and all ancestors of `p`.
void free_family(person *p)
{
    // Handle base case
    if (p == NULL)
    {
        return;
    }

    // Free parents recursively
    free_family(p->parents[0]);
    free_family(p->parents[1]);

    // Free child, by now, all parents are freed by the recursive call.
    free(p);
}

// Print each family member and their alleles.
void print_family(person *p, int generation)
{
    // Handle base case
    if (p == NULL)
    {
        return;
    }

    // Print indentation
    for (int i = 0; i < generation * INDENT_LENGTH; i++)
    {
        printf(" ");
    }

    // Print person
    if (generation == 0)
    {
        printf("Child (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }
    else if (generation == 1)
    {
        printf("Parent (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }
    else
    {
        for (int i = 0; i < generation - 2; i++)
        {
            printf("Great-");
        }
        printf("Grandparent (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }

    // Print parents of current generation
    print_family(p->parents[0], generation + 1);
    print_family(p->parents[1], generation + 1);
}

// Randomly chooses a blood type allele.
char random_allele()
{
    int r = rand() % 3;
    if (r == 0)
    {
        return 'A';
    }
    else if (r == 1)
    {
        return 'B';
    }
    else
    {
        return 'O';
    }
}
