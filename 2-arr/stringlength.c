#include<stdio.h>
#include<cs50.h>
#include<string.h>

/*
There are 4 stages in compiling:
1. Preprocessing: expanding macros, removing comments,
    and generating the appropriate include files - replace #include with function prototypes found in header files (usually comes with C compiler).

2. Compilation: translation of source code into assembly code for a specific target architecture.

3. Assembly: converting the assembly code into machine code, which is a series of binary instructions that the computer can understand.

4. Linking: combines all of machine code from multiple files into a single executable program, also resolves any external references, such as linking to libraries or system calls.

Note: there are no so called built-in functions in C language. The C standard library provides the basic functions. The compiler is responsible for translating C into machine code.
The first C compiler could be written in some other language. The libraries themselves can be written in C.
*/

int string_length (string s);

int main ()
{
    string s = get_string("input: ");

    // int length = strlen(s) *strlen is a function in string.h*
    int length = string_length(s);
    printf("%i\n", length);
}

int string_length (string s)
{
    int i = 0;
    // \0 is nul value which is an extra byte of info stored in memory to signal the end of a string.
    while (s[i] != '\0')
    {
        i++;
    }
    return i;
}