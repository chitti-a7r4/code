#include <stdio.h>

int main(){
    char hello[] = "Hello world";
    hello[0] = 'J';
    // must use only single quotes to modify a string
    printf("%s\n", hello);
}