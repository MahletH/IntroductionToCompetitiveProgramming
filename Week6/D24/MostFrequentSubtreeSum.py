# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTreeSum(self, root: TreeNode, col: dict) -> int:
        if(not root.left and not root.right):
            if root.val not in col:
                col[root.val]=1
            else:
                col[root.val]+=1
            return root.val
        elif(not root.left):
            sum1=root.val+self.findTreeSum(root.right,col)
            if sum1 not in col:
                col[sum1]=1
            else:
                col[sum1]+=1
            return sum1
        elif(not root.right):
            sum1=root.val+self.findTreeSum(root.left,col)
            if sum1 not in col:
                col[sum1]=1
            else:
                col[sum1]+=1
            return sum1
        else:
            sum1=root.val+self.findTreeSum(root.right,col)+self.findTreeSum(root.left,col)
            if sum1 not in col:
                col[sum1]=1
            else:
                col[sum1]+=1
            return sum1
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        col={}
        self.findTreeSum(root,col)
        maxOccur=0
        lst=[]
        for i in col:
            if col[i]==maxOccur:
                lst.append(i)
            elif col[i]>maxOccur:
                lst=[]
                lst.append(i)
                maxOccur=col[i]
        return lst
     
