#include<stdio.h>

void draw_pyramid(int n)
{
    if(n <= 0)
    {
        return;
    }
    // this line will be sub with the whole function, until n == 0, and it will stop at the previous line.
    // let's say n is 2, this line will become
    // draw_pyramid(1) ----> draw_pyramid(0) ----> this will return ----> for-loop printing out # as now n = 1.
    // for-loop printing out ## as for now n = 2.
    draw_pyramid(n - 1);

    for(int i = 0; i < n; i++)
    {
        printf("#");
    }
    printf("\n");
}


int main()
{
    int n;
    int * pn = &n;
    printf("How many layers: ");
    scanf("%i", pn);

    draw_pyramid(n);
}