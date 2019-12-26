x=input()
y=x.split(" ")
row=int(y[0])//int(y[2])
col=int(y[1])//int(y[2])
if(int(y[0])%int(y[2])>0):
    row+=1
if(int(y[1])%int(y[2])>0):
    col+=1

print(row*col)


