#include <stdio.h>

int main(){
    int age= 40;
    int* y = &age;
    printf(" Your age %d\n",age);
    printf(" Your age %p\n",&age); //also gives pointer
    // Reference
    printf(" Your age %p\n",y);
    // Dereference
    printf("Your age %d\n",*y);
    
}