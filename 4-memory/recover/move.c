#include<stdio.h>
#include<stdlib.h>

int main()
{
    char *name = malloc(8 * sizeof(char));
    char *newname = malloc(8 * sizeof(char));
    for(int i = 0; i < 50; i++)
    {
        sprintf(name, "%03i.jpg", (i + 1));
        sprintf(newname, "jpg/%03i.jpg", (i + 1));
        rename(name, newname);
    }

    free(name);
    free(newname);
    return 0;
}