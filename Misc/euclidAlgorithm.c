// Computes the greatest common divisor of two numbers using the 
// Euclidian Algorithm
// Braden Carlson 09/21/2021

#include <stdio.h>
#include <math.h>

void gcd( int x, int y);
int max( int x, int y);
int min( int x, int y);

int quotients[50];
int remainders[50];

int main( void ) {
	


    int number1;
	int number2;
	printf("%s", "Enter the two integers: ");
	scanf("%d %d", &number1, &number2);
	gcd(number1,number2);
    puts("");

   
	
}



void gcd( int x, int y) {
    // finds the absolute values of the numbers passed into the method,
    // then finds the maximum and minimum, and assigns those values
    // x and y, where the original values of x and y are now stored in aOrig and bOrig.	
    int a = fabs(x);
    int b = fabs(y);
	int maximum = max(a,b);
	int minimum = min(a,b);
    int aOrig = x;
    int bOrig = y;
	x = maximum;
	y = minimum;

    // if a was negative: set aFlipped to true
    // similar for b
    _Bool aFlipped = 0;
    _Bool bFlipped = 0;
    if (aOrig==-fabs(aOrig)) {
        aFlipped = 1;
    }
    if (bOrig==-fabs(bOrig)) {
        bFlipped = 1;
    }

	int q = 0;
	unsigned int r = 0;
    unsigned int count = 0;
    
    // Computes each step of the division algorithm, until there is no
    // remainder left. Note that this algorithm only uses the positive 
    // values of the original integers passed to the method.
    while ( x % y != 0 ) {
		q = x / y;
		r = x % y;
        quotients[count] = q;
        remainders[count] = r;
		printf("%d = %d * %d + %d\n", x, q, y, r);
		x = y;
		y = r;
        count++;
	} // end while loop
	printf("%d = %d * %d\n", x, x/y, y);
    int x1 = 1;
    int y1 = -quotients[--count];



   

    



    // uncomment this line and the prinf statment in the following
    // for loop to see and test the values produced by the backsubstitutions
    // from the Euclidean Algorithm.
    // printf("%d %d\n", x1, y1);
    for (int i = 1 ; i <= count ; i++) {
	    if (i % 2 == 1) {
            x1=x1-quotients[count-i]*y1;  
        } 
        else if (i % 2 == 0 ) {
			y1=y1-quotients[count-i]*x1;
        } // end if.
	    // printf("%d %d\n", x1, y1);
    } // end for loop.
    
    // enter a blank line between the steps and the results.
    puts("");
    
    // depending on which of the two integers, if any, were negative,
    // print out the results as neccessary.
    if ( aFlipped==1 && bFlipped==0 ) {
            printf("gcd(%d,%d)=%d\n", -a, b, y);
    } else if ( aFlipped==0 && bFlipped==1) {
        printf("gcd(%d,%d)=%d\n", a, -b, y);
    } else if ( aFlipped==1 && bFlipped==1 ) {
        printf("gcd(%d,%d)=%d\n", -a, -b, y);
    } else if ( aFlipped==0 && bFlipped==0 ) {
        printf("gcd(%d,%d)=%d\n", a, b, y);
    }
    
    // depending on which of the two integers, if any, were negative,
    // print out the corresponding linear combination that equals
    // their gcd.
    if (a*x1+b*y1==y) {
        if ( aFlipped==1 && bFlipped==0 ) {
            printf("%d(%d)+%d(%d)=%d\n", -x1, -a, y1, b, y);
        } else if ( aFlipped==0 && bFlipped==1) {
            printf("%d(%d)+%d(%d)=%d\n", x1, a, -y1, -b, y);
        } else if ( aFlipped==1 && bFlipped==1 ) {
            printf("%d(%d)+%d(%d)=%d\n", -x1, -a, -y1, -b, y);
        } else if ( aFlipped==0 && bFlipped==0 ) {
            printf("%d(%d)+%d(%d)=%d\n", x1, a, y1, b, y);
        }
    } else if (a*y1+b*x1==y) {
        if ( aFlipped==1 && bFlipped==0 ) {
            printf("%d(%d)+%d(%d)=%d\n", -y1, -a, x1, b, y);
        } else if ( aFlipped==0 && bFlipped==1) {
            printf("%d(%d)+%d(%d)=%d\n", y1, a, -x1, -b, y);
        } else if ( aFlipped==1 && bFlipped==1 ) {
            printf("%d(%d)+%d(%d)=%d\n", -y1, -a, -x1, -b, y);
        } else if ( aFlipped==0 && bFlipped==0 ) {
            printf("%d(%d)+%d(%d)=%d\n", y1, a, x1, b, y);
        }
    } // end if statement.
    
    // print out their least common multiple.
    printf("lcm(%d,%d)=%d\n", a, b, a*b/y);


    
	
} // end gcd method.

int max( int x, int y) {
	return x > y ? x : y;
}

int min( int x, int y) {
	return x > y ? y : x;
}
