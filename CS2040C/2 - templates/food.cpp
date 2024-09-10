#include "food.h"
#include <iostream>
using namespace std;

Food Food:: operator+(const Food& rhs) const
{
    return Food(this -> m_name + " " + rhs.m_name, this -> m_calories + rhs.m_calories);
}


bool Food:: operator<(const Food& rhs) const
{
    return true;
}

bool Food:: operator==(const Food& rhs) const
{
    return true;
}
