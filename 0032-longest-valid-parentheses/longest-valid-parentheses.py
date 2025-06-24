class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = [-1]
        max_ = 0

        for i, a in enumerate(s):
            if a == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_ = max(max_, i - stack[-1])

        return max_

        