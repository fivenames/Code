#include<cs50.h>
#include<stdio.h>

int main()
{
    long card;
    do
    {
        card = get_long("Card Number: ");
    }
    while (card <= 0);

    int c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16;

    c1 = card % 10;
    c2 = (card % 100) / 10;
    c3 = (card % 1000) / 100;
    c4 = (card % 10000) / 1000;
    c5 = (card % 100000) / 10000;
    c6 = (card % 1000000) / 100000;
    c7 = (card % 10000000) / 1000000;
    c8 = (card % 100000000) / 10000000;
    c9 = (card % 1000000000) / 100000000;
    c10 = (card % 10000000000) / 1000000000;
    c11 = (card % 100000000000) / 10000000000;
    c12 = (card % 1000000000000) / 100000000000;
    c13 = (card % 10000000000000) / 1000000000000;
    c14 = (card % 100000000000000) / 10000000000000;
    c15 = (card % 1000000000000000) / 100000000000000;
    c16 = (card % 10000000000000000) / 1000000000000000;

    int c_even, c_odd;

    c_even = ((c2 * 2) % 10) + (((c2 * 2) % 100) / 10) + ((c4 * 2) % 10) + (((c4 * 2) % 100) / 10) + ((c6 * 2) % 10) + (((c6 * 2) % 100) / 10) + ((c8 * 2) % 10) + (((c8 * 2) % 100) / 10) + ((c10 * 2) % 10) + (((c10 * 2) % 100) / 10) + ((c12 * 2) % 10) + (((c12 * 2) % 100) / 10) + ((c14 * 2) % 10) + (((c14 * 2) % 100) / 10) + ((c16 * 2) % 10) + (((c16 * 2) % 100) / 10);
    c_odd = (c1 + c3 + c5 + c7 + c9 + c11 + c13 + c15);

    int c_total;

    c_total = (c_even + c_odd);

    if((c_total % 10) != 0)
    {
        printf("Invalid card number\n");
    }
    else
    {
        if(c13 == 4 && c16 == 0)
        {
            printf("VISA\n");
        }
        else
        {
            if(c16 == 4)
            {
                printf("VISA\n");
            }
            else
            {
                if(c16 == 5)
                {
                    printf("MASTERCARD\n");
                }
                else
                {
                    if(c15 == 3 && c16 == 0)
                    {
                        printf("AMERICAN EXPRESS\n");
                    }
                    else
                    {
                        printf("UNKNOWN TYPE\n");
                    }
                }
            }
        }
    }
}