class Solution:
    def tribonacci(self, n: int) -> int:
        lst={}
        return self.rec(n,lst)
    def rec(self,n: int,lst: dict) -> int:
        if n in lst:
            return lst[n]
        if(n==0):
            lst[0]=0
            return 0
        elif n==1 or n==2:
            lst[1]=1
            lst[2]=1
            return 1
        else:
            lst[n]=self.rec(n-1,lst)+self.rec(n-2,lst)+self.rec(n-3,lst)
            return lst[n]

def main():
    while True:
        try:
            n = int(input());
            
            ret = Solution().tribonacci(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
