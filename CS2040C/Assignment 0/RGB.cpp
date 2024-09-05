#include "RGB.h"
#include <cmath>
#include <iostream>

#define BOUND(x, min, max) ((x) < (min) ? (min) : ((x) > (max) ? (max) : (x)))

RGB::RGB(int red, int green, int blue) :
    red_(BOUND(red, 0, 255)),
    green_(BOUND(green, 0, 255)),
    blue_(BOUND(blue, 0, 255)) { }

RGB::~RGB() { }

void RGB::print() {
    std::cout << "RGB(" << red_ << ", " << green_ << ", " << blue_ << ")"
    << std::endl;
}

RGB RGB::mix(const RGB& other) {
    int result[3] = {0};
    result[0] = other.red() + this->red();
    result[1] = other.green() + this->green();
    result[2] = other.blue() + this->blue();

    for(int i = 0; i < 3; i++){
        if(result[i] < 0){
            result[i] = 0;
        }
        else if(result[i] > 255){
            result[i] = 255;
        }
    }
    
    return RGB(result[0], result[1], result[2]);
}

RGB RGB::scale(double factor) {
    int result[3] = {0};
    result[0] = round(this->red() * factor);
    result[1] = round(this->green() * factor);
    result[2] = round(this->blue() * factor);

    for(int i = 0; i < 3; i++){
        if(result[i] < 0){
            result[i] = 0;
        }
        else if(result[i] > 255){
            result[i] = 255;
        }
    }
    
    return RGB(result[0], result[1], result[2]);
}
