class Solution:
    def isValid(self, s: str) -> bool:
        br = {'(': ')', '[': ']', '{': '}'}
        stack = []
        
        for char in s:
            if char in br:  # opening bracket
                stack.append(char)
            else:  # closing bracket
                if not stack:  # stack empty → invalid
                    return False
                top = stack.pop()
                if br[top] != char:
                    return False
        
        return len(stack) == 0
