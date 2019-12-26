test=eval(input())
words=[]
for i in range(test):
    word=input()
    words.append(word)
ans=[]
for word in words:
    lst=word.split(" ")
    a=int(lst[0])
    b=int(lst[1])
    c=int(lst[2])
    r=int(lst[3])
    if(a>b):
        a,b=b,a
    tot=0
    l=c-r
    u=c+r
    if(a<l):
        if(b<l):
            tot+=b-a
        else:
            tot+=l-a
    if(u<b):
        if(a>u):
            tot=b-a
        else:
            tot+=b-u
    ans.append(tot)
for i in ans:
    print(i)
