#include <stdio.h>

int main(){
    int length;
    printf("Please enter your length here: \n");
    scanf("%d",&length);
    int breadth;
    printf("Please enter your breadth here \n");
    scanf("%d",&breadth);
    int area = length * breadth;
    printf("Your area is %d ",area);
}