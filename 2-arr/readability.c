#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main()
{
    float index;
    //important to set as float even though they are just int.
    float words = 1.0, letters = 0.0, sentences = 0.0;

    string text = get_string("Text: ");

    int i, j, k;

    int n = strlen(text);

    for(i = 0; i < n; i++)
    {
        if(text[i] == ' ')
        {
            words += 1;
        }
        else
        {
            words += 0;
        }
    }

    for(j = 0; j < n; j++)
    {
        // isalpha returns non-zero int if the input is an alphabet, which will be interpreted as 'true' by the computer. While a return of zero will be interpreted as false.
        if(isalpha(text[j]) != 0)
        {
            letters += 1;
        }
        else
        {
            letters += 0;
        }
    }

    for(k = 0; k < n; k++)
    {
        if(text[k] == '.' || text[k] == '?' || text[k] == '!')
        {
            sentences += 1;
        }
        else
        {
            sentences += 0;
        }
    }

    float L, S;

    int grade;
    // if letters, words and sentences are set as int, when they divide each other, the ans will be int, hence a BUG will occur.
    L = letters / words * 100;

    S = sentences / words * 100;

    index = 0.0588 * L - 0.296 * S - 15.8;

    grade = round(index);

    if(grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        if(grade >= 1 && grade <= 16)
        {
            printf("Grade %i\n", grade);
        }
        else
        {
            if(grade > 16)
            {
                printf("Grade 16+\n");
            }
        }
    }


}
