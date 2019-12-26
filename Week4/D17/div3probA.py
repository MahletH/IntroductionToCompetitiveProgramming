test=eval(input())
words=[]
for i in range(test):
    word=input()
    words.append(word)
ans=[]
for word in words:
    lst=word.split(" ")
    a=abs(int(lst[0])-int(lst[1]))
    b=abs(int(lst[0])-int(lst[2]))
    c=abs(int(lst[1])-int(lst[2]))
    s=a+b+c
    if(s<4):
        s=0
    else:
        s=s-4
    ans.append(s)
for i in ans:
    print(i)
