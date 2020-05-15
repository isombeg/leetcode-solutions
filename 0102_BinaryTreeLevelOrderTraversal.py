# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if(root == None):
            return []
        
        rslt = []
        queueA = [root]
        queueB = []
        counter = 0
        
        while not(len(queueA) == 0):
            rslt.append([])
            
            for elem in queueA:
                if elem.left != None:
                    queueB.append(elem.left)
                if elem.right != None:
                    queueB.append(elem.right)
                rslt[counter].append(elem.val)
            
            queueA = queueB
            queueB = []
            counter += 1
        
        return rslt