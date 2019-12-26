class Solution:
    def firstBadVersion(self, n):
        return self.badVersion(n,1)
    def badVersion(self, n, m):
        mid=(n+m)//2
        if(n==m):
            return n
        flag=isBadVersion(mid)
        if(flag):
            return self.badVersion(mid, m)
        else:
            return self.badVersion(n, mid+1)
          
def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = int(line);
            line = next(lines)
            bad = int(line);
            
            ret = Solution().firstBadVersion(n, bad)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
