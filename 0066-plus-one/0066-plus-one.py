class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nd=[]
        x=len(digits)
        sum=0
        for i in range (x):
            sum=(sum+digits[i])*10
        sum=sum//10
        sum+=1
        s=str(sum)
        c=len(s)
        for i in range(c):
            a=s[i]
            z=int(a)
            nd.append(z)
        return(nd)
