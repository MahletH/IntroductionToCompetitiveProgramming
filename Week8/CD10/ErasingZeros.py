test=eval(input())
for i in range(test):
    word=input()
    prev,ctr=0,0
    on,off=0,0
    for i in word:
        if i=='1' and not on:
            on=1
        if on and i=='0':
            ctr+=1
        if on and ctr and i=='1':
            prev+=ctr
            ctr=0
            
    print(prev)
