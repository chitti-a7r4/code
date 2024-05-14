#include <stdio.h>

int main(){
    int number;
    printf("please enter your number: \n");
    scanf("%i", &number);

    if (number % 2 == 0 ){
        printf("Your number is even");
    }
    else printf("Your number is odd");

}