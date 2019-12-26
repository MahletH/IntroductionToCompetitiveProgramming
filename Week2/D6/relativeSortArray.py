def relativeSortArray(arr1,arr2):
        arr3=[]
        arr4=[]
        for i in arr2:
            for j in arr1:
                if(i==j):
                    arr3.append(j)
        for j in arr1:
            if(j not in arr3):
                arr4.append(j)
        arr4.sort()
        for j in arr4:        
            arr3.append(j)
        return arr3
    
