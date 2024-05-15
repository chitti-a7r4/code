#include <stdio.h>

int main(){
    int age[] = {18,20, 40, 77, 108, 5};
    size_t total = sizeof(age)/sizeof(age[0]);
    int i;
    int sum = 0;
    for ( i = 0; i < total; i++)
    {
        sum += age[i];
    }
    float average = (float) sum/ total;
    printf("Your average age is : %.3f\n", average);
    


}