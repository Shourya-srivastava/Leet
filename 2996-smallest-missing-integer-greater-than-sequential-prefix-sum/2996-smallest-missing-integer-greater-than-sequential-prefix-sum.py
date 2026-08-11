class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum=0
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]+1):
                sum=sum+nums[i]

  
            else:
                break
        a=nums[0]
        sum=sum+int(a)
        nums.sort()
        for j in range (len(nums)):
            if (nums[j]==sum):
                sum+=1
        return sum

