#include <stdio.h>

int main(){
    char name[30];
    // specify the number of characters the name can hold
    printf("Please enter your name \n");
    fgets(name,sizeof(name),stdin);
    // Here stdin means standard input just like scanf
    printf("Welcome, %s", name);

}