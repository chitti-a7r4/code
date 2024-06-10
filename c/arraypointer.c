#include <stdio.h>

int main(){
    int array[4] = {10, 20, 30, 40};
    int* pointer = array;
    int i;
    for ( i = 0; i < 4; i++)
    {
        printf("%d\n",*(pointer+ i));
    }   
    
}