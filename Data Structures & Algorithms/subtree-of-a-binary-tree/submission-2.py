# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkMatch(r1, r2) -> bool:
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            if r1.val == r2.val:
                return checkMatch(r1.left, r2.left) and checkMatch(r1.right, r2.right)
            
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if checkMatch(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)