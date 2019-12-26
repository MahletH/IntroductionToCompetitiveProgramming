def count(lst):
    listOfOccur=[]
    for i in range(10):   
        listOfOccur.append(0)
    for j in lst:
        listOfOccur[j]+=1
    for j in range(1,len(listOfOccur)):
        listOfOccur[j]=listOfOccur[j]+listOfOccur[j-1]
    return listOfOccur

def counting_sort(orlst,lst):
    occur=count(lst)
    sortedList=[]
    sortedList1=[]
    for i in range(len(lst)):
        sortedList.append(0)
        sortedList1.append(0)
    for i in range(len(lst)):
        k=lst[len(lst)-1-i]
        k1=orlst[len(lst)-1-i]
        j=occur[k]-1
        occur[k]=occur[k]-1
        sortedList[j]=k
        sortedList1[j]=k1
    return sortedList1
def radix_sort(lst):
    maxNum=max(lst)
    k=1
    while(maxNum//10!=0):
        k+=1
        maxNum=maxNum//10
    copy=[]
    for i in lst:
        copy.append(i)
    for j in range(1,k+1):
        cutLst=[]
        for i in range(len(lst)):   
            cutLst.append(copy[i]%10)
        lst=counting_sort(lst,cutLst)
        for i in range(len(lst)):   
            copy[i]=lst[i]//(10**j)
        k-=1
    return lst
print(radix_sort([33,21,56,23,58,105,90,0]))
