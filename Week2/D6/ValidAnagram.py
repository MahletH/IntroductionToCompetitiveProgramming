class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        words=[]
        for i in t:
            words.append(i)
        for i in s:
            if(i not in words):
                return False
            words.remove(i)
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
            line = next(lines)
            t = stringToString(line);
            
            ret = Solution().isAnagram(s, t)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
