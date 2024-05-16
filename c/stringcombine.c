#include <stdio.h>
#include <string.h>

int main(){
    char line1[] = "Hello";
    char line2[] = "World";
    
    strcat(line1,line2);
    // same like this use strcpy to copy a string from one to other 

    printf("%s\n", line1);

}