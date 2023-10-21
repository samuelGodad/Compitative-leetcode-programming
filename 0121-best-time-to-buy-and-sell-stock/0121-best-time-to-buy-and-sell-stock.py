class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # maxProfit=0
        # low=prices[0]
        # for price in prices:
        #     if price<low:
        #         low=price
        #     maxProfit=max(maxProfit,price-low)
        # return maxProfit
        maxprofit=0
        left,right=0,1
        while right <len(prices):
            if prices[left]<prices[right]:
                profit=prices[right]-prices[left]
                maxprofit=max(profit,maxprofit)
            else:
                left =right
            right+=1
        return maxprofit
    
        
