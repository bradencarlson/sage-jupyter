// program that calculates a^b (mod n)
// Implementing the repeated squares algorithm.

// This is version 2.0! Using unsigned long long ints instead of unsigned ints.

// Braden Carlson
// 10/11/2021

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void toBinary(unsigned long long int exponent, unsigned long long int binary[], size_t size);
void printArray(unsigned long long int array[],size_t size);
void repeatedSquares(unsigned long long int base, unsigned long long int modulus, unsigned long long int squares[], size_t size);
unsigned long long int binaryExponentiation(unsigned long long int n, unsigned long long int squares[], unsigned long long int binary[], size_t size);

int main( void ) {
    unsigned long long int a = 0;
    unsigned long long int b = 0;
    unsigned long long int n = 0;


    // get values to be used in computation from user.    
    printf("%s", "To calculate a^b (mod n):\n");
    printf("%s", "Please enter a: ");
    scanf("%llu", &a);
    printf("%s", "Please enter b: ");
    scanf("%llu", &b);
    printf("%s", "Please enter n: ");
    scanf("%llu", &n);

    // calculate the approximate size of the exponent in binary
    // and declare an array to hold the bits in binary of the number b.
    unsigned long long int size = (int) ceil(log(b)/log(2))+1;
    unsigned long long int binary[size];

    // call toBinary function to convert the exponent into binary
    toBinary(b, binary, size);

    // declare an appropriately sized array to hold the repeated squares.
    unsigned long long int squares[size];

    // call repeatedSquares method to calculate all of a^(2^k) necessary.
    repeatedSquares(a, n, squares, size);


    // call binaryExponentiation method to calculate the final result of the 
    // repeated squares algorithm.
    unsigned long long int result = binaryExponentiation(n,squares, binary, size);
    printf("%llu^%llu = %llu (mod %llu)\n", a, b, result, n);
}

// compute the binary representation of b, and save it (in reverse) to the array
// passed to the method.
void toBinary(unsigned long long int b, unsigned long long int c[], size_t size) {
    unsigned long long int q = 1;
    unsigned long long int r = 0;
    unsigned long long int index = 0;    
    while (index < size) {
        q = b / 2;
        r = b % 2;
        b = q;
        c[index] = r;
        index++;
    }
}

// compute a^(2^k) (mod n) up to the necessary value of k, and save them to the 
// array squares passed into the method.  
void repeatedSquares(unsigned long long int a, unsigned long long int n, unsigned long long int squares[], size_t size) {
    unsigned long long int temp = a;
    squares[0] = a % n;   
    for(int i = 1; i<size ; i++) {
        squares[i] = ((squares[i-1]*squares[i-1]) % n);
    }
}

// Compute the final result, using all the necessary powers of a, and multiplying them,
// reducing mod n along the way, to calculate a^b (mod n).
unsigned long long int binaryExponentiation(unsigned long long int n, unsigned long long int squares[], unsigned long long int binary[], size_t size) {
    unsigned long long int result = 1;    
    for(int i = 0; i<size ; i++) {
        if(binary[i]!=0) {
            result *= squares[i];
            result = result % n;
        }
    }
    return result;
}

// method to print an unsigned long long int array.
void printArray(unsigned long long int c[],size_t size) {
    for( int i = 0; i < size; i++) {
        printf("%4llu ", c[i]);
    }
    puts("");
}
