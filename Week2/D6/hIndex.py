def hIndex(citations):
    h=0
    for i in range(1,len(citations)+1):
        ctr=0
        for j in range(len(citations)):
            if(citations[j]>=i):
                ctr+=1
        if(ctr>=i):
            h=i
    return h
print(hIndex([3,0,6,1,5]))
