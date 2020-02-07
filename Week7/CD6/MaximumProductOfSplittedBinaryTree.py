# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getSums(self, root: TreeNode, col:dict) -> int:
        if(not root):
            return 0
        if(root in col):
            return col[root]
        col[root]=root.val+self.getSums(root.right,col)+self.getSums(root.left,col)
        return col[root]  
    def getProducts(self, root: TreeNode, col:dict, lst:List[int], tot:int) -> None:
        if(not root):
            return
        lst.append((tot-col[root])*col[root])
        self.getProducts(root.left,col,lst,tot)
        self.getProducts(root.right,col,lst,tot)
    
    def maxProduct(self, root: TreeNode) -> int:
        col={}
        self.getSums(root,col)
        lst=[]
        tot=col[root]
        self.getProducts(root,col,lst,tot)
        res=max(lst)%(10**9+7)
        return res
