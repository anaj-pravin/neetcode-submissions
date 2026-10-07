class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_prof = prices[0]

        for i in range(1, len(prices)):
            if curr_prof > prices[i]:
                curr_prof = prices[i]
                continue
            # profit.append(prices[i] - curr_prof)
            profit = max(profit, prices[i] - curr_prof)

        # if profit:
        #     return max(profit)
        # return 0
        return profit