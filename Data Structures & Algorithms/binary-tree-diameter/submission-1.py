# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def treeHeight(node: TreeNode) -> int:
            if node == None:
                return 0
            return 1 + max(treeHeight(node.left), treeHeight(node.right))
        
        if root == None: 
            return 0
        left_height = treeHeight(root.left)
        right_height = treeHeight(root.right)
        return max(max(left_height + right_height, self.diameterOfBinaryTree(root.left)), self.diameterOfBinaryTree(root.right))
        
        