#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *source,*target;
    source = fopen("abc.txt","r");
    target = fopen("xyz","w");
    char ch;
    int count=0;
    if(source==NULL||target==NULL){
        printf("Error");
        exit(0);
    }
 
    while(1){
        ch = fgetc(source);
        if(ch==EOF){
            break;
        }
        else{
            count++;
        fputc(ch,target);
        }
    }

    printf("number of character are %d\n",count);
    printf("Copied successfully\n");

    fclose(source);
    fclose(target);

}