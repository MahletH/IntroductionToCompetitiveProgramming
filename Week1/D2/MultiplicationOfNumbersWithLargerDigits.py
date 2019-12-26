def addTwoNumber(x,y):
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

def multiply(x,y):
    listOfPro=[];       
    if(len(x)>=len(y)):
        productOfNum=""
        k=1
        r=0
        while(k<=len(y)):
            j=1
            while(j<=len(x)):
                product=int(x[len(x)-j])*int(y[len(y)-k])+r
                if(product//10==0):
                    r=0
                    productOfNum=str(product)+productOfNum
                else:
                    productOfNum=str(product%10)+productOfNum
                    r=product//10
                j+=1
            
            if (r!=0):
                productOfNum=str(r)+productOfNum
            productOfNum=productOfNum+"0"*(k-1)
            listOfPro.append(productOfNum)
            productOfNum=""
            k+=1
    i=0
    sumOfPro="0"
    while(i<len(listOfPro)):
        sumOfPro=addTwoNumber(sumOfPro,listOfPro[i])
        i+=1
    return sumOfPro
x=input("Enter the first number: ")
y=input("Enter the second number: ")
if(x[0]=="-" and y[0]=="-"):
    x=x[1:]
    y=y[1:]
    added=multiply(x,y)
    print(added)
elif(x[0]=="-"):
    x=x[1:]
    added=multiply(x,y)    
    added="-"+added
    print(added)
elif(y[0]=="-"):
    y=y[1:]
    added=multiply(x,y)    
    added="-"+added
    print(added)
else:
    added=multiply(x,y)   
    print(added)
      
    
