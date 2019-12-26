def partition(lst, start, end):
    pos = start+1
    piv=start 
    i=end
    while(i>=pos):   
        if lst[i] < lst[piv]:
            lst[i],lst[pos] = lst[pos],lst[i]  
            pos += 1
            i+=1
        i-=1
    lst[pos-1],lst[piv] = lst[piv],lst[pos-1] 
    return pos-1

def quick_sort(lst, start, end):
    if start < end:                   
        pos = partition(lst, start, end)
        quick_sort(lst, start, pos - 1)
        quick_sort(lst, pos + 1, end)
    return lst
list1=[33,21,56,23,58,105,90,0]
print(quick_sort(list1,0,len(list1)-1))
