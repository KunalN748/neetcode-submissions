class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maximum = 0
        if len(prices) < 2:
            return maximum

        while right != len(prices):        
            if prices[right] < prices[left]:
                left = right
                right += 1
            else: 
                maximum = max(maximum, prices[right]-prices[left])        
                right += 1
        return maximum