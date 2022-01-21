// program that calculates a^b (mod n)
// Implementing the repeated squares algorithm.

// Braden Carlson
// 10/11/2021

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void toBinary(unsigned int exponent, unsigned int binary[], size_t size);
void printArray(unsigned int array[],size_t size);
void repeatedSquares(unsigned int base, unsigned int modulus, unsigned int squares[], size_t size);
unsigned int binaryExponentiation(unsigned int n, unsigned int squares[], unsigned int binary[], size_t size);

int main( void ) {
    unsigned int a = 0;
    unsigned int b = 0;
    unsigned int n = 0;


    // get values to be used in computation from user.    
    printf("%s", "To calculate a^b (mod n):\n");
    printf("%s", "Please enter a: ");
    scanf("%u", &a);
    printf("%s", "Please enter b: ");
    scanf("%u", &b);
    printf("%s", "Please enter n: ");
    scanf("%u", &n);

    // calculate the approximate size of the exponent in binary
    // and declare an array to hold the bits in binary of the number b.
    unsigned int size = (int) ceil(log(b)/log(2))+1;
    unsigned int binary[size];

    // call toBinary function to convert the exponent into binary
    toBinary(b, binary, size);

    // declare an appropriately sized array to hold the repeated squares.
    unsigned int squares[size];

    // call repeatedSquares method to calculate all of a^(2^k) necessary.
    repeatedSquares(a, n, squares, size);


    // call binaryExponentiation method to calculate the final result of the 
    // repeated squares algorithm.
    unsigned int result = binaryExponentiation(n,squares, binary, size);
    printf("%u^%u = %u (mod %u)\n", a, b, result, n);
}

// compute the binary representation of b, and save it (in reverse) to the array
// passed to the method.
void toBinary(unsigned int b, unsigned int c[], size_t size) {
    unsigned int q = 1;
    unsigned int r = 0;
    unsigned int index = 0;    
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
void repeatedSquares(unsigned int a, unsigned int n, unsigned int squares[], size_t size) {
    unsigned int temp = a;
    squares[0] = a % n;   
    for(int i = 1; i<size ; i++) {
        squares[i] = ((squares[i-1]*squares[i-1]) % n);
    }
}

// Compute the final result, using all the necessary powers of a, and multiplying them,
// reducing mod n along the way, to calculate a^b (mod n).
unsigned int binaryExponentiation(unsigned int n, unsigned int squares[], unsigned int binary[], size_t size) {
    unsigned int result = 1;    
    for(int i = 0; i<size ; i++) {
        if(binary[i]!=0) {
            result *= squares[i];
            result = result % n;
        }
    }
    return result;
}

// method to print an unsigned int array.
void printArray(unsigned int c[],size_t size) {
    for( int i = 0; i < size; i++) {
        printf("%4u ", c[i]);
    }
    puts("");
}
