def substruct(x,y):
    sumOfNum=""
    zeros=len(x)-len(y)
    y=("0"*zeros)+y
    sumOfNum=""
    j=1
    r=0
    while(j<=len(y)):
        if(int(x[len(x)-j])>=int(y[len(y)-j])):
           sum=int(x[len(x)-j])-int(y[len(y)-j])
        else:
           sum=10+int(x[len(x)-j])-int(y[len(y)-j])
           r=1
        sumOfNum=str(sum)+sumOfNum
        if(r==1):
            temp=int(x[len(x)-j-1])-1
            if(temp!=-1):                    
                x=x[:len(x)-j-1]+str(temp)+x[len(x)-j:]
            else:
                k=j+1
                carry=9
                while(temp==-1):
                    temp=int(x[len(x)-k])-1
                    if(k==2):
                        x=x[:len(x)-k+1]+str(carry)
                    else:
                        x=x[:len(x)-k+1]+str(carry)+x[len(x)-k+2:]
                    k+=1 
                x=x[:len(x)-k+1]+str(temp)+x[len(x)-k+2:]               
            r=0
        j+=1
        
    
    return sumOfNum
def whichIsGreater(x,y):
    num=0
    while(num<len(x)):
        if(x[num]>y[num]):
            return x
        elif(x[num]<y[num]):
            return y
        num+=1
    return ""

def addTwoPositiveNumber(x,y):
    if(len(x)>=len(y)):
        zeros=len(x)-len(y)
        y=("0"*zeros)+y
        sumOfNum=""
        j=1
        r=0
        while(j<=len(y)):
            sum=int(x[len(x)-j])+int(y[len(y)-j])+r
            if(sum//10==0):
                r=0
                sumOfNum=str(sum)+sumOfNum
            else:
                sumOfNum=str(sum%10)+sumOfNum
                r=1
            j+=1
        if (r==1):
            sumOfNum="1"+sumOfNum
    elif(len(x)<len(y)):
        sumOfNum=""
        zeros=len(y)-len(x)
        x=("0"*zeros)+x
        
        j=1
        r=0
        while(j<=len(x)):
            sum=int(x[len(x)-j])+int(y[len(y)-j])+r
            if(sum//10==0):
                r=0
                sumOfNum=str(sum)+sumOfNum
            else:
                sumOfNum=str(sum%10)+sumOfNum
                r=1
            j+=1
        
        if (r==1):
            sumOfNum="1"+sumOfNum
    return sumOfNum
def checkForZeros(added):
    checkZero=0
    signed=False
    if(added[0]=="-"):
        signed=True
        added=added[1:]
    while(checkZero<len(added)-1):
        if(added[checkZero]=="0"):
            added=added[checkZero+1:]
        else:
            break
    if(signed and added[0]!="0"):
        added="-"+added
    return added
x=input("Enter the first number: ")
y=input("Enter the second number: ")
added=""
if(x[0]=="-" and y[0]=="-"):
    x=x[1:]
    y=y[1:]
    added=addTwoPositiveNumber(x,y)
    added="-"+added
##    print(added)
elif(x[0]=="-"):
    x=x[1:]
    if(len(y)>len(x)):
        added=substruct(y,x)
    elif(len(y)<len(x)):
        added="-"+substruct(x,y)
    else:
        greater=whichIsGreater(x,y)
        if(greater==x):
            added="-"+substruct(x,y)
        elif(greater==y):
            added=substruct(y,x)
        else:
            added="0"
##    print(added)
elif(y[0]=="-"):
    y=y[1:]    
    if(len(x)>len(y)):
        added=substruct(x,y)
    elif(len(x)<len(y)):
        added="-"+substruct(y,x)
    else:
        greater=whichIsGreater(x,y)
        if(greater==x):
            added=substruct(x,y)
        elif(greater==y):
            added="-"+substruct(y,x)
        else:
            added="0"
##    print(added)
else:
    added=addTwoPositiveNumber(x,y)
##    print(added)
added=checkForZeros(added)
print(added)   


    
