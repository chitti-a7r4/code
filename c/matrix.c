#include <stdio.h>

int main(){
    int arr1[50],arr2[50],r1,r2,c1,c2;
    printf("Enter a matrix\n");
    for(int i=0;i<r1;i++){
        for(int j=0;j<c1;j++){
            printf("enter elements a%d%d",i+1,j+1);
            scanf("%d",&arr1[i]);
        }
    }
    for(int i=0;i<r2;i++){
        for(int j=0;j<c2;j++){
            printf("enter elements b%d%d",i+1,j+1);
            scanf("%d",&arr2[i]);
        }
    }
    for(int i=0;i<r1;i++){
        for(int j=0;j<c1;j++){
            printf("entered elements are\n");
            printf("%d ",&arr1[i]);
        }
    }
    for(int i=0;i<r2;i++){
        for(int j=0;j<c2;j++){
            printf("entered elements are\n");
            printf("%d ",&arr2[i]);
        }
    }
}