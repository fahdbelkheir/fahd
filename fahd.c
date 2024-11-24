#include <stdio.h>
#include <stdbool.h>
#include <math.h>


bool numprime(int N) {
    if (N <= 1) return false;       
    if (N <= 3) return true;  
    if (N % 2 == 0 || N % 3 == 0) return false; 


}

int main() {
    int number;

    printf("Enter an integer: ");
    scanf("%d", &number);
    if (numprime(number)) {
        printf("%d is a prime number.\n", number);
    } else {
        printf("%d is not a prime number.\n", number);
    }

    return 0;
}