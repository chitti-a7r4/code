#include <stdio.h>

int main(){
    int startPopulation;
    printf("Please enter starting Population \n ");
    scanf("%d", &startPopulation);
    int endPopulation;
    printf("Please enter ending Population \n");
    scanf("%d", &endPopulation);
    if (startPopulation >= 9 & startPopulation<endPopulation)
    {
        int years = 0;
        int currentPopulation = startPopulation;
        while (currentPopulation<endPopulation)
        {
            int born = currentPopulation/3;
            int died = currentPopulation/4;
            currentPopulation = currentPopulation + born - died;
            years++;

        }
        printf("No of years %d\n", years);
        
       
    }
    else{
        printf("Please enter a startpopulation greater than or equal to 9 and Endpopulation greater than startpopulation");
    }
    
    
}