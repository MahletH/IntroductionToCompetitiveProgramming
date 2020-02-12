class Node:
    def __init__(self):
        self.lst=[None]*26
        self.isEndOfWord=False
class Solution:
    def helper(self, root:Node, lst:List[str], word:str) ->None:
        if not root.isEndOfWord:
            return
        lst.append(word)
        for i in range(len(root.lst)):
            if root.lst[i] and root.lst[i].isEndOfWord:
                c=chr(ord('a')+i)
                self.helper(root.lst[i],lst,word+c)
        
    def longestWord(self, words: List[str]) -> str:
        root=Node()
        root.isEndOfWord=True
        for word in words:
            curr=root
            for c in word:
                if curr.lst[ord(c)-ord('a')]:
                    curr=curr.lst[ord(c)-ord('a')]
                else:
                    new_node=Node()
                    curr.lst[ord(c)-ord('a')]=new_node
                    curr=new_node
            curr.isEndOfWord=True
        lst=[]
        self.helper(root,lst,"")
        prevMax=""
        for w in lst:
            if len(w)>len(prevMax):
                prevMax=w
        return prevMax
        
        
                    
