class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        n = len(prices)
        curr_prof = 101

        for i in range(n):
            if curr_prof > prices[i]:
                curr_prof = prices[i]
                continue
            profit.append(prices[i] - curr_prof)

        if profit:
            return max(profit)
        return 0