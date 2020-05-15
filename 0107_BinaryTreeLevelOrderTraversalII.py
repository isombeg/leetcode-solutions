# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # Special case:
        if root == None:
            return []
        
        queueA, queueB = [root], []
        rslt = []
        while len(queueA) > 0:
            rslt.insert(0,[])
            while len(queueA) > 0:
                if queueA[0].left != None:
                    queueB.append(queueA[0].left)
                if queueA[0].right != None:
                    queueB.append(queueA[0].right)
                rslt[0].append(queueA.pop(0).val)
            queueA = queueB.copy()
            queueB = []
        return rslt
            
                    