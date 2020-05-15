# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def maxD(root):
    a,b = 0,0
    
    # Base case
    if root.left == None and root.right == None:
        return 1
    
    if root.left != None:
        a = maxD(root.left)
    if root.right != None:
        b = maxD(root.right)
    
    if a > b:
        return a + 1
    else:
        return b + 1

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if(root == None):
            return 0
        return maxD(root)