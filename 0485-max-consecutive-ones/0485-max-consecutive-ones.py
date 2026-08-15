from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count1 = 0   
        count2 = 0          
        for i in nums:
            if i == 1:
                count1 += 1
                count2 = max(count2, count1)  
            else:
                count1 = 0 
        return count2
