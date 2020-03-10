# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self,node,col,depth):
        if not node:
            return 
        elif depth in col:
            col[depth].append(node.val)
        else:
            col[depth]=[node.val]
        self.dfs(node.left,col,depth+1)
        self.dfs(node.right,col,depth+1)
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        col={}
        self.dfs(root,col,0)
        ans=[]
        for i in range(len(col)-1,-1,-1):
            ans.append(col[i])
        return ans
