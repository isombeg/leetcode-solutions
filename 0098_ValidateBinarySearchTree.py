# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def inOrderTrav(node, l):
    if(node.left != None):
        l = inOrderTrav(node.left,l)
    l.append(node.val)
    if(node.right != None):
        l = inOrderTrav(node.right,l)
        
    return l

def validList(a):
    if(len(a) > 1):
        for i in range(1,len(a)):
            if(a[i] <= a[i-1]):
                return False
    return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if(root == None):
            return True
        
        arr = inOrderTrav(root,[])
        return validList(arr)