listOfNum=[2,5,6,8,4,9,5,43,45,21]
for i in range(1,len(listOfNum)):
    temp=listOfNum[i]
    j=i-1
    while(j>=0):
        if(temp<listOfNum[j]):
            listOfNum[j+1]=listOfNum[j]
            listOfNum[j]=temp
        j-=1
        
        
print(listOfNum)
