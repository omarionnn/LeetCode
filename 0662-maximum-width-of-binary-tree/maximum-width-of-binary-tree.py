# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 0)])
        maxxie = 0

        while q:
            node, left_pos = q[0]
            right = -1
            length = len(q)
            for i in range(length):
                curr, pos = q.popleft()

                if i == length - 1:
                    right = pos

                if curr.left:
                    q.append((curr.left, 2 * pos))
                if curr.right:
                    q.append([curr.right, 2 * pos + 1])

            maxxie = max(maxxie, right - left_pos + 1)

        return maxxie


        