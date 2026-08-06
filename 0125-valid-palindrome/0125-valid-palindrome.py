class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean="".join(char for char in s if char.isalnum())
        clean1=clean.lower()
        a=clean1[::-1]
        if(clean1==a):
            return True
        else :
            return False