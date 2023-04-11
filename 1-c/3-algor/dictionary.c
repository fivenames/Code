#include<stdio.h>
#include<string.h>

/*
This is called a dictionary data structure, implemented by a key and a value, such that the key will always lead to the value.
*/

typedef struct
{
    char* name;
    char* number;
}
person;

int main()
{
    person phonenum[2];

    phonenum[0].name = "Carter";
    phonenum[0].number = "+65-12345678";

    phonenum[1].name = "David";
    phonenum[1].number = "+1-949-468-2750";

    // Define string by one-dimensional char array. Memory is allocated automatically.
/*
char* cannot be used unless, assigning it a string literal: char * str = "Hello, world!" or Dynamically allocating memory for it using the malloc function.
Pointer is a value of memory address stored in memory. Without defining the address where the pointer points, the value is just some garbage value, and scanf cannot access.
*/
    char str[20];
    printf("Name: ");

/*
The scanf() function returns the number of variable successfully matched and assigned, rather then the read value itself (in this case 1; the str varaible),
it dereference the variable and changes it's initial value, however if a wrong data type is input, scanf returns 0 and the variable retain it's initial value.

The square brackets indicate a scan set, which is a way of specifying a set of characters to match in the input string.
The '^' symbol inside the square brackets negates the set, meaning that the scan set matches any character that is not in the set.
Hence any character that is not '\n' will be read and stored.

Adding an integer after the '%' as width specifier will limit the number of value that scanf reads. "%69[^\n]" will read up to 69 chars.

scanf can also be used to scan more than one variable example: scanf("%d %d", &x, &y); this will return 2.
*/
    scanf("%[^\n]", str);

    for(int i = 0; i < 2; i++)
    {
        if(strcmp(phonenum[i].name, str) == 0)
        {
            printf("Found: %s\n", phonenum[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}