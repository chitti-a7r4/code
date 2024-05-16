#include <stdio.h>
#include <string.h>

int main(){
    char line1[] = "Wi";       
    char line2[] = "Hi";       
    char line3[] = "Horld";

    printf("%d\n", strcmp(line1,line2));
    printf("%d\n", strcmp(line1, line3));       
 }