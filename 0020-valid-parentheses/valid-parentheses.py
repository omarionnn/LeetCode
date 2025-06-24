class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 0:
            return True
        
        
        
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')' and (len(stack) == 0 or stack[-1] != '('):
                return False
            elif char == ']' and (len(stack) == 0 or stack[-1] != '['):
                return False
            elif char == '}' and (len(stack) == 0 or stack[-1] != '{'):
                return False
            else:
                stack.pop()
                
                
        if len(stack) == 0:
            return True
        else:
            return False
                                  