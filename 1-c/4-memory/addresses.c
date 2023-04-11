#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n;

/*
the memory address printed out is the value of the pointer of n.
the 0x in front of the int is by convention assigned to represent that this is a hexadecimal (Hex), memory addresses are described commonly by Hex.
Hex has 16 numbers per digit. where 'A' comes after '9' meaning ten, and so on till 'F'.
*/

    // Here the & operator will give the memory address of the variable it comes with.
    printf("The memory address:%p\nThe size is %lubytes\n", &n, sizeof(n));

    char x = ' ';
    // Here the * operator will represent that the data type of the variable it comes with is an address.
    char *p = &x;

    // Here the * operator will give the data stored in the memory location of the address.
    printf("%c", *p);

    char *str = "That's all for now.";

    // Notice here that the str given to printf is an address, it will print out all the data from this address till a NUL value.
// If * operator is used the function will print out a single char instead, be it first letter *str or second letter *(str + 1) and so on.
    printf("%s", str);
// To print out from the second or subsequent letter of the string, pointer arithmetic can used. Example: (str + 1) will print out the second letter till NUL.

    return 0;
}

// NULL is an address of 0, the very first byte in memory which nothing should be going in there by convention.

// Usage: valgrind ./addresses