#include <stdio.h>

int main(){
    int array[] = {1,2,3,4,5};
    size_t length = sizeof(array) / sizeof(array[0]);
    int i;

    for ( i = 0; i < length; i++)
    {
        printf("%zu\n", array[i]);
    }
    

}    
