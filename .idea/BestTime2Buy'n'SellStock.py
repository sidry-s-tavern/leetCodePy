class Solution:
    """
    TODO: Time Limit Exceeded 200 / 212 testcases passed
    """
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if profit < max(prices[i + 1:]) - prices[i]:
                profit = max(prices[i + 1:]) - prices[i]
        return profit


print(Solution.maxProfit(Solution, [7, 1, 5, 3, 6, 4]))
