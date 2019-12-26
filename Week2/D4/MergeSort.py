def mergeSort(lst):   
    if len(lst) > 1:
        s1= 0
        s2 = 0
        mid = len(lst) //2
        s1= lst[:mid]
        s2= lst[mid:]
        n=len(lst)
        print(s1,s2)
        mergeSort(s1)
        mergeSort(s2)
        i =j=k= 0
        while i < len(s1) and j < len(s2):
            if s1[i] < s2[j]:
                lst[k] = s1[i]
                i = i + 1                
            else:
                lst[k] = s2[j]
                j = j + 1
            k = k + 1
        while i < len(s1):
            lst[k] =s1[i]
            i = i + 1
            k = k + 1

        while j < len(s2):
            lst[k] = s2[j]
            j = j + 1
            k = k + 1
    return lst
lst=[2,5,6,8,4,9,43]
print(mergeSort(lst))    

