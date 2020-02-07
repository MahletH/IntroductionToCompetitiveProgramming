# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self, root: TreeNode,lst :List[int]) -> None:
        if(root):
            self.inorder(root.left,lst)
            lst.append(root.val)
            self.inorder(root.right,lst)                       
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        lst=[]
        if(not root1 and not root2):
            return lst
        elif(not root1):
            self.inorder(root2,lst)
            return lst
        elif(not root2):
            self.inorder(root1,lst)
            return lst
        lst1=[]
        lst2=[]
        self.inorder(root1,lst1)
        self.inorder(root2,lst2)
        lst=lst1+lst2
        lst.sort()
        return lst
