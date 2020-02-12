class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        line=1
        tot=0
        for i in S:
            c=ord(i)-ord('a')
            if tot+widths[c]<=100:
                tot+=widths[c]
            else:
                line+=1
                tot=widths[c]
        lst=[line,tot]
        return lst
