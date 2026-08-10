class Solution:
    def isValid(self, s: str) -> bool:

        t = []   
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                t.append(s[i])
            else:
                if len(t) == 0:  
                    return False
                if s[i] == ')' and t[-1] == '(':
                    t.pop()
                elif s[i] == ']' and t[-1] == '[':
                    t.pop()
                elif s[i] == '}' and t[-1] == '{':
                    t.pop()
                else:
                    return False
        if len(t) == 0:
            return True
        else:
            return False