"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def rootLength(self,root: 'Node',l: int, lsts: List[int]) -> int:        
        l+=1
        lst=root.children
        if(not len(lst)):
            lsts.append(l)
            return l
        for i in lst:
            self.rootLength(i,l,lsts)
        
        
    def maxDepth(self, root: 'Node') -> int:
        if(not root):
            return 0
        maxDep=0
        lst=[]
        self.rootLength(root,maxDep,lst)
        return max(lst)
