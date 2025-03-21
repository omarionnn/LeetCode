# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        returner = 0

        res = float('-inf')
        q = deque()
        q.append(root)

        while q:
            level += 1
            
            level_total = 0

            for i in range(len(q)):
                curr = q.popleft()
                level_total += curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            if level_total > res:
                res = level_total
                returner = level

        return returner
        