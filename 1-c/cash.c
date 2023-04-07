#include<cs50.h>
#include<stdio.h>

int main()
{
    int amount;

    do
    {
        amount = get_int("Number of cents: ");
    }
    while(amount < 0);

    int quarters;

    quarters = amount / 25;

    int dimes;

    dimes = (amount - (quarters * 25)) / 10;

    int nickels;

    nickels = (amount - (quarters * 25) - (dimes * 10)) / 5;

    int pennies;

    pennies = (amount - (quarters * 25) - (dimes * 10) - (nickels * 5)) / 1;

    printf("%i quarters, %i dimes, %i nickels, %i pennies\n", quarters, dimes, nickels, pennies);
}