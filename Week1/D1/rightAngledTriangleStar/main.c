#include <stdio.h>

int main()
{
    int input, numOfRows, numOfStar;
    printf("Enter number of rows:\n");
    scanf("%d",&input);
    for(numOfRows=1; numOfRows<=input; ++numOfRows){
        for(numOfStar=1; numOfStar<=numOfRows; ++numOfStar){
            printf("*\t");
        }
        printf("\n");
    }
    return 0;
}
