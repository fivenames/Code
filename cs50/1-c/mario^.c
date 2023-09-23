#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("n= ");
    }
    while (n < 1 || n > 8);

    int i;
    for ( i = 0; i < n; i++ )
    {
        int s;
        for (s = 0; s < n - i - 1; s++)
        {
            printf(" ");
        }

        int j;
        for (j = 0; j <= i; j++)
        {
            printf("#");
        }

        // include 2 spaces after the right alligned pyramid
        printf("  ");

        // make a left alligned pyramid after the right alligned one.
        for (j = 0; j <= i; j++)
            {
            printf("#");
            }

        printf("\n");
    }

    return 0;
}