test=eval(input())
arr=[]
for i in range(test):
    lst=input()
    arr.append(lst)
ans=[]
ans2=[]
for lst in arr:
    l,r,u,d=0,0,0,0
    path=[0]*2
    for i in lst:
        if i=="L":
            l+=1
        elif i=="R":
            r+=1
        elif i=="U":
            u+=1
        else:
            d+=1
    if l<r:
        r=l
    else:
        l=r
    if u<d:
        d=u
    else:
        u=d
    if l==0 and u!=0  or l!=0 and u==0:
        if l==0:
            path=[0,0,1,1]
        else:
            path=[1,1,0,0]
        ans2.append(path)
        ans.append(2)
    else:
        path=[l,r,u,d]
        ans2.append(path)
        ans.append(l+r+u+d)
    ##if abs(l-d)<=1:
for i in range(len(ans)):
    print(ans[i])
    path=""
    direct=ans2[i]
    l="L"*direct[0]
    r="R"*direct[1]
    u="U"*direct[2]
    d="D"*direct[3]
    path=l+u+r+d
    print(path)
    
    
    ##else:
    ##    if l>d:
            
    
