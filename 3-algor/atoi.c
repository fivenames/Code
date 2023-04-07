#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int my_atoi(char *x);

int main(void)
{
    char *x = malloc(sizeof(char) * 8);
    printf("Enter a positive integer: ");
    scanf("%s", x);

    int y = my_atoi(x);

    printf("%d\n", (y));
    free(x);
}

int my_atoi(char *x)
{
    int n = strlen(x);
    int y = (x[n - 1] - '0');
    x[n - 1] = '\0';

    // notice that the strlen did not decrease yet after the setting of NUL character, as strlen is called before that step.
    if (n == 1)
    {
        return y;
    }

    y = y + my_atoi(x) * 10;

    return y;
}