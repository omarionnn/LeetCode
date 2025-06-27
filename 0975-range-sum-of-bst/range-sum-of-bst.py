# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        count = 0
        if not root:
            return 0

        if low <= root.val <= high:
            count += root.val

        count += self.rangeSumBST(root.left, low, high)
        count += self.rangeSumBST(root.right, low, high)

        return count

        
        