# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        #print(t1)
        if(t1==None):
            return t2
        if(t2==None):
            return t1
        newRoot=TreeNode(t1.val+t2.val)
        if(t1.left!=None and t2.left!=None):
            newRoot.left=self.mergeTrees(t1.left,t2.left)
        
        if(t1.left!=None and t2.left==None):
            newRoot.left=t1.left
        elif(t2.left!=None and t1.left==None):
            newRoot.left=t2.left
        if(t1.right!=None and t2.right!=None):
            newRoot.right=self.mergeTrees(t1.right,t2.right)
            #print(t1.right.val)
            #print(newRoot)
        else:
                #print(newRoot)
            if(t1.right!=None and t2.right==None):
                newRoot.right=t1.right
                #print(newRoot)
            elif(t2.right!=None and t1.right==None):
                newRoot.right=t2.right
                #print(newRoot)
        return newRoot
