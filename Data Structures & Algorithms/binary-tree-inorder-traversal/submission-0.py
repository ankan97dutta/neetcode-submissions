# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder(self, root: Optional[TreeNode], acc: List[int]):
        if not root:
            return 
        
        self.inorder(root.left, acc)
        acc.append(root.val)
        self.inorder(root.right, acc)


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        output = []

        self.inorder(root, output)
        return output 
        