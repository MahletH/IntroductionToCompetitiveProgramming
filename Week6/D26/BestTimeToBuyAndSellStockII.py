### Leetcode problem solution found at:'https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/'
class Solution:
    def profit(self, prices: List[int],trans: int) -> int:    
        if(len(prices)==0):
            return trans
        minNum,maxNum=prices[0],prices[0]
        minInd,maxInd=0,0
        for i in range(minInd+1,len(prices)):
            if(prices[i]<=minNum):
                minNum=prices[i]
                minInd=i
            elif(prices[i]>minNum):
                maxNum=prices[i]
                maxInd=i
                break
        for i in range(maxInd+1,len(prices)):
            if(prices[i]>maxNum):
                maxNum=prices[i]
                maxInd=i
            else:
                break
        if(minInd<maxInd):
            trans+=maxNum-minNum
            return self.profit(prices[maxInd+1:],trans)
        return trans
    def maxProfit(self, prices: List[int]) -> int:
        return self.profit(prices,0)
