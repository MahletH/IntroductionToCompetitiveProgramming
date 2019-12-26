#include <stdio.h>
#include <stdlib.h>

int main()
{
    int input, numOfRows, numOfStar;
    void printSpaces(int numOfRows);
    printf("Enter number of rows:\n");
    scanf("%d",&input);
    int temp=input;
    for(numOfRows=1; numOfRows<=input; numOfRows++){
        printSpaces(temp);
        for(numOfStar=1; numOfStar<numOfRows*2; numOfStar++){
            printf("*");
        }
        temp--;
        printf("\n");
    }
    return 0;
}
void printSpaces(int numOfrows){
    for(int i=1; i<numOfrows;i++){
        printf(" ");
    }
}
