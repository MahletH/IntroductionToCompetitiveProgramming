class Solution:
    def power(self, i: int, x: int, col: dict) -> None:
        prev=col[i-1]
        col[i]=prev*x        
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if(bound<2):
            return []
        xcol={0:1}
        ycol={0:1}
        i,j=0,0
        sum1=0
        lst=[]
        if(x==1 and y==1):
            lst.append(2)
        elif(x==1):
            while(ycol[j]<bound):
                j+=1
                self.power(j,y,ycol)
            for l in range(j):
                sum1=1+ycol[l]
                lst.append(sum1)
        elif(y==1):
            while(xcol[i]<bound):
                i+=1
                self.power(i,x,xcol)
            for l in range(i):
                sum1=1+xcol[l]
                lst.append(sum1)
        else:
            while(xcol[i]<bound):
                i+=1
                self.power(i,x,xcol)

            while(ycol[j]<bound):
                j+=1
                self.power(j,y,ycol)
            for k in range(i):
                for l in range(j):
                    sum1=xcol[k]+ycol[l]
                    if (sum1<=bound and sum1 not in lst):
                        lst.append(sum1)
        return lst
