# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        bool1=True
        if(p==None and q==None):
            return True
        elif(p==None or q==None):
            return False
        elif(p.left==None and p.right==None and q.left==None and q.right==None):
            if(p.val==q.val):
                return True
            else:
                return False
        if(p.left!=None and q.left==None or p.right!=None and q.right==None):
            return False
        elif(p.left==None and q.left!=None or p.right==None and q.right!=None):
            return False
        if(p.val==q.val):
            if(p.left!=None and q.left!=None):
                if(bool1==False):
                    return False
                bool1=self.isSameTree(p.left,q.left)
                
            if(p.right!=None and q.right!=None):
                if(bool1==False):
                    return False
                bool1=self.isSameTree(p.right,q.right) 
            
            #elif(p.left==None and q.left==None and p.right==None and q.right==None):
                #return True
        elif(p.val!=q.val):
            return False
        return bool1
