def isBeautiful(words):
    lst=[]
    for word in words:        
        chars=[]
        if(len(word)==1):
            if(word[0]=="?"):
                chars.append("a")
            else:
                chars.append(word[0])
            lst.append(chars)
            continue
        un=[]
        flag=False
        for i in range(len(word)-1):
            if word[i]!="?" and word[i+1]!="?" :
                if word[i]==word[i+1]:
                    lst.append(-1)
                    flag=True
                    break
        if(flag):
            falg=False
            continue
        for j in range(len(word)):
            if word[j] =="?":
                un.append(j)
            chars.append(word[j])
        for i in un:
            if i==0:
                pos=chars[i+1]
                if pos=="a" or pos=="b":
                    chars[i]="c"
                else:
                    chars[i]="a"
            elif(i==len(word)-1):
                pre=chars[i-1]
                if pre=="a" or pre=="b":
                    chars[i]="c"
                else:
                    chars[i]="a"
            else:
                pre=chars[i-1]
                pos=chars[i+1]
                if (pre=="a" and pos=="b") or (pre=="b" and pos=="a") :
                    chars[i]="c"
                elif (pre=="a" and pos=="c") or (pre=="c" and pos=="a") :
                    chars[i]="b"
                elif (pre=="c" and pos=="b") or (pre=="b" and pos=="c") :
                    chars[i]="a"
                else:
                    if(pre=="a" or pre=="b"):
                        chars[i]="c"
                    else:
                        chars[i]="a"                    
        lst.append(chars)
    return lst
numWords=eval(input())
words=[]
for i in range(numWords):
    word=input()
    words.append(word)
lst=isBeautiful(words)
an=[]
for j in lst:
    if j==-1:
        an.append(j)
    else:
        st=""
        for k in j:
            st=st+k
        an.append(st)
for j in an:
    print(j)
