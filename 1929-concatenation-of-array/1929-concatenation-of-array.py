class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = len(nums)
        b=a
        i=0
        while(b!=0):
            nums.append(nums[i])
            i+=1
            b=b-1
        return nums

