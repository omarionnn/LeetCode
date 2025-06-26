class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                subs = ''
                while stack and stack[-1] != '[':
                    subs = stack.pop() + subs
                stack.pop()

                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * subs)

        return ''.join(stack)
        