#include <stdio.h>

int main(){
    int array[] = {1,2,3,4,5};
    int size = sizeof(array)/sizeof(array[2]);
    // instead of using int , we can use size_t , and instead of %lu , we can use %zu
    printf("%lu\n", size);

}