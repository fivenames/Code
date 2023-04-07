// problem set 1 mario(less comfortable)

#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    // continue to prompt the user to key in n if n condition not met.
    do
    {
        n = get_int("n= ");
    }
    while (n < 1 || n > 8);

    int i;
    for ( i = 0; i < n; i++ )
    {
        // find relationship between the number of spaces needed to print before printing #, which is s=n-i-1.
        int s;
        for (s = 0; s < n - i - 1; s++)
        {
            printf(" ");
        }

        // to make a left alligned pyramid the number of # on the role = to the role number, hence j=i.
        int j;
        for (j = 0; j <= i; j++)
        {
            printf("#");
        }

    // make new line outside the loop.
    printf("\n");
    }

    return 0;
}