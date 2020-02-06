class Solution:
    def climbStairs(self, n: int) -> int:
        if(n<2):
            return 1
        lst1=[0]*n
        lst2=[0]*n
        lst1[0],lst2[0],lst1[1],lst2[1]=0,1,1,2
        i=2
        while(i<n):
            lst1[i]=lst1[i-1]+lst1[i-2]
            lst2[i]=lst2[i-1]+lst1[i]
            i+=1
        return lst2[-1]
