def isBeautiful(words,numList):
    word=words
    n=numList
    lst1=[]
    for k in range(len(word)):
        w=word[k]
        wlst=[0]*len(w)
        isBeautiful=""
        for i in range(len(w)):
            wlst[int(w[i])-1]=i+1
        minIndex=len(w)
        maxIndex=0
        for i in range(len(wlst)):
            if(wlst[i]<minIndex):
               minIndex=wlst[i]
            if(wlst[i]>maxIndex):
               maxIndex=wlst[i]
            if(maxIndex-minIndex+1==i+1):
                isBeautiful=isBeautiful+"1"
            else:
                isBeautiful=isBeautiful+"0"
        lst1.append(isBeautiful)
    return lst1
        
numWords=eval(input())
words=[]
numlst=[]
for i in range(numWords):
    num=eval(input())
    word=input()
    words.append(word.split(" "))
    numlst.append(num)
lst=isBeautiful(words,numlst)
an=[]
for j in lst:
    st=""
    for k in j:
        st=st+str(k)
    an.append(st)
for j in an:
    print(j)
