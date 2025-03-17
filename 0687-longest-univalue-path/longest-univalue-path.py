# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(root):
            nonlocal longest
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            left_a = right_a = 0

            if root.left and root.left.val == root.val:
                left_a = left + 1

            if root.right and root.right.val == root.val:
                right_a = right + 1

            longest = max(longest, left_a + right_a)
            return max(left_a, right_a)

        dfs(root)
        return longest
        