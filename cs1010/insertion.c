// sort a sequence of number (not expressed in array) in descending order. *Without the use of arrays and loops.
// eg. input: 1010 | output: 1100

#include <stdio.h>
#include <stdlib.h>

int insert(int num, int digit);
int sort(int num);

int main(void){
    int num = 0;
    printf("sequence: ");
    scanf("%i", &num);
    
    num = sort(num);
    printf("%i", num);
    
    return 0;
}

// return the sequence with the inserted digit.
int insert(int num, int digit){
    // if digit is bigger than the first digit of the sequence, just return the digit from the top of the stack frame.
    if(num == 0){
        return digit; // returned value down the frame will be multiplied by 10 to append the original sequence.
    }
    if(digit <= num % 10){ // if digit smaller than the last digit of the sequence, append the digit
        return num * 10 + digit;
    } // else recursively remove the last digit from sequence, check again and append the removed digit to the right of the sequence.
    return ( insert(num / 10, digit) * 10 ) + (num % 10);
}

// return the sequence sorted in descending order.
int sort(int num){
    if(num < 10){ // if the sequence has only one digit, return the sequence.
        return num;
    } // else recursively remove the last digit from the sequence and insert into the sequence.
    return insert(sort(num / 10), num % 10);
    /*
        the recursion works by diving into the top of the stack frame, where only the first digit of the sequence remain, insert() will then sort the second digit with the first.
        This result will be returned to the sort() function call inside the insert() function, resulting in a already sorted sequence to be inserted with the next diigit.
    */
}