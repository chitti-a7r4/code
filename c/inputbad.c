#include <stdio.h>

int main(){
    char name[30];
    printf("Please enter your name\n ");
    scanf("%s", &name);
    printf("Welcome, %s \n",name);
}
// this code does not work if we type our name with space so we need to use other function