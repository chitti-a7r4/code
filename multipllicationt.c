#include <stdio.h>

int main(){
    int i = 2;
    int j;
    for ( j = 1; j <= 10; j+= 1)
    {
        // printf("%d\n", i);
        int sum = i * j;
        printf("2 * %d = %i\n ", j ,sum);
    }
    
}