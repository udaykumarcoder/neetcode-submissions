class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force
        # maxim=0
        # for i in range(len(prices)-1):
        #     j=i+1
        #     while(j<len(prices)):
        #         if(prices[j]-prices[i]>maxim):
        #             maxim=prices[j]-prices[i]
        #         j=j+1
        # return maxim

        #optimal 
        min_price=prices[0]
        max_profit=0
        for price in prices[1:]:
            max_profit=max(max_profit,price-min_price)
            min_price=min(min_price,price)
        return max_profit
