listOfNum=[2,5,6,8,4,9,5,43,45,21]
for i in range(len(listOfNum)):
    minNum=listOfNum[i]
    firstNum=listOfNum[i]
    minIndex=i
    for j in range(i+1,len(listOfNum)):
        if(minNum>listOfNum[j]):
            minNum=listOfNum[j]
            minIndex=j
    listOfNum[i]=minNum
    listOfNum[minIndex]=firstNum
        
        
print(listOfNum)
