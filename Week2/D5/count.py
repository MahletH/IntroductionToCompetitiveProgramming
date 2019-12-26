def count(lst):
    maxNum=max(lst)+1
    listOfOccur=[0]*maxNum
    for j in lst:
        listOfOccur[j]+=1
    return listOfOccur

def counting_sort(lst):
    occur=count(lst)
    sortedList=[]
    for i in range(len(occur)):
        if occur[i]!=0:
            for j in range(occur[i]):
                sortedList.append(i)
    return sortedList
list1=[33,21,56,23,58,105,90,0,21]
print(counting_sort(list1))
