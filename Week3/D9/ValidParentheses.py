class Solution:
    def isValid(self, s: str) -> bool:
        lst=[]
        openning=["[","(","{"]
        closing=["}",")","]"]
        k=len(s)
        op,cl=0,0
        for j in s:
            if j in openning:
                lst.append(j)
                op+=1
            else:
                if(len(lst)==0):
                    return False
                i=lst.pop()
                cl+=1
                if i=="[" and j!="]":
                    return False
                elif i=="(" and j!=")":
                    return False
                elif i=="{" and j!="}":
                    return False
        if(op!=cl):
            return False
        return True

def stringToString(input):
    import json

    return json.loads(input)

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
            s = stringToString(line);
            
            ret = Solution().isValid(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
