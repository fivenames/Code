#include<stdio.h>
#include<string.h>

typedef struct
{
    char * name;
    int votes;
}
person;

//*argv[] is an array of memory addresses of char.
int main(int argc, char *argv[])
{
    person candidate[argc -1];

    for(int i = 0; i < argc - 1; i++)
    {
        candidate[i].votes = 0;
        candidate[i].name = argv[i + 1];
    }

    int voters;
    printf("Number of voters (Max 9): ");
    //& operator is needed to pass the memory address of the variable. A function called will use a different part of memory, an address is needed to change the memory in main().
    scanf("%i", &voters);

    for(int i = 0; i < voters; i++)
    {
        //This is an array of string.
        //Defined by a two dimensional char array, consists of 'voters' number of string and a max of 256 characters each, with remaining uninitiallised values as garbage values.
//Using [256] is ok because when printf is called it will print until '\0'. However, for variables like Int, this will not work as printf will print all of them.
//Using char * str[] will cause runtime error such as "Segmentation fault (core dumped)". In this case - the programme is tring to write to an invalid memory address.
        char vote[voters][256];
        printf("Vote: ");
        //& operator is not needed here as arrays are always passed to functions as pointer. However, the name of the array is not a memory address stored in memory.
        scanf("%s", vote[i]);

        int counter = 0;

        for(int j = 0; j < argc - 1; j++)
        {
            if(strcmp(vote[i], candidate[j].name) == 0)
            {
                candidate[j].votes++;
                break;
            }
            else
            {
                counter++;
            }
        }

        if(counter == (argc - 1))
        {
            printf("Candidate not found\n");
            return 1;
        }
    }

    int highestvotes_idx = 0;

    for(int i = 1; i < argc - 1; i++)
    {
        if(candidate[i].votes > candidate[highestvotes_idx].votes)
        {
            highestvotes_idx = i;
        }
    }

    for(int i = 0; i < argc - 1; i++)
    {
        if(candidate[i].votes == candidate[highestvotes_idx].votes)
        {
            printf("Winner: %s\n", candidate[i].name);
        }
    }

    return 0;
}