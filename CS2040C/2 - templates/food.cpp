#include "food.h"
#include <iostream>
using namespace std;

Food Food:: operator+(const Food& rhs) const
{
    // modify this function
    return Food("", 0);
}


bool Food:: operator<(const Food& rhs) const
{
    return true;
}

bool Food:: operator==(const Food& rhs) const
{
    return true;
}
