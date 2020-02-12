test=eval(input())
for i in range(test):
    w=input()
    lst=w.split(" ")
    n,g,b=int(lst[0]),int(lst[1]),int(lst[2])
    k=(n+1)//2
    l=k/g
    if int(l)!=l:
        res=k+int(l)*b
        if(res>=n):
            print(int(res))
        else:
            remO=g*(int(l+1)-l)+b
            remI=n-res
            if remI<=remO:
                res+=remI
                print(int(res))
            else:
                print(n)
    else:
        res=k+int(l-1)*b
        if(res>=n):
            print(int(res))
        else:
            print(n)
