#include <stdio.h>

int main(){
    int array[] = {1,2,3,4,5};
    int size = sizeof(array)/4;

    printf("%lu\n", size);
}