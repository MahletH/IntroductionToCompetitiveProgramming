# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if(not root):
            return None
        stack=[]
        temp=root
        par,res=None,None
        while(len(stack) or temp):
            if(temp):
                stack.append(temp)
                temp=temp.left
            else:
                temp=stack.pop()
                if(not par):
                    res=TreeNode(temp.val)
                    par=res
                else:
                    res.right=TreeNode(temp.val)
                    res=res.right
                temp=temp.right
        return par
