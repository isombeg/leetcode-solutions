# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def sum(n, temp):
    if n.left == None and n.right == None:
        return 10 * temp + n.val
    
    a,b = 0,0
    if n.left != None:
        a = sum(n.left, 10*temp + n.val)
    if n.right != None:
        b = sum(n.right, 10*temp + n.val)
    
    return a+b

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return sum(root,0)