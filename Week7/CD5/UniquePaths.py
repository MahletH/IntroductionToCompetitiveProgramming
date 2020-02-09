class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if(m==1 or n==1):
            return 1
        m-=1
        n-=1
        lst1=[]
        lst=[]
        for i in range(n):
            for j in range(m):
                if(not i):
                    lst1.append(2+j)
                elif(not j):
                    lst1.append(2+i)
                else:
                    lst1.append(2)
            lst.append(lst1)
            lst1=[]
        for i in range(1,n):
            for j in range(1,m):
                lst[i][j]=lst[i-1][j]+lst[i][j-1]
        return lst[n-1][m-1]
