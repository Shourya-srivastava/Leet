class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        a=len(prices)-1
        for i in range (a):
            if (prices[i]<prices[i+1]):
                profit+=prices[i+1]-prices[i]
            else:
                i+=1
        return profit



                