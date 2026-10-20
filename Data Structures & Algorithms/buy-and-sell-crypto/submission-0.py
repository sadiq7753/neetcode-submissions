class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):

                curr_min = 0
                curr_max = 0
                if prices[i] < prices[j]:
                    profit = max((prices[j]- prices[i]), profit)
        return profit            
