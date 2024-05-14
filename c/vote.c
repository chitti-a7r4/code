#include <stdio.h>

int main(){

   int userage;
   printf("Please enter your age: \n");
   scanf("%d", &userage);
   int votingage = 18; 
   if (userage > votingage)
   {
    printf("You are eligible to vote");
   }
   else printf("Grow up lil bro");
   
}