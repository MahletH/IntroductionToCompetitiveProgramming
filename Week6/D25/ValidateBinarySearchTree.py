# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root.left and not root.right:
                return root.val,root.val,True
            if root.left and not root.right:
                check=dfs(root.left)
                if check[1]<root.val and check[2]:
                    return check[0],root.val,True
                return check[0],root.val,False
            if root.right and not root.left:
                check=dfs(root.right)
                if check[0]>root.val and check[2]:
                    return root.val,check[1],True
                return root.val,check[0],False
            left_check=dfs(root.left)
            right_check=dfs(root.right)
            if left_check[1]<root.val and left_check[2] and right_check[0]>root.val and right_check[2]:
                return left_check[0],right_check[1],True
            return left_check[1],right_check[0],False
        if not root:
            return True
        return dfs(root)[2]
