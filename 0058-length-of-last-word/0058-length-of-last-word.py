class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        b=a[-1]
        c=len(b)
        return c
        