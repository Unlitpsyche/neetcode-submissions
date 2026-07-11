class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i = 0
        j = 1
        while j < len(prices):
            if prices[j] > prices[i]:
                ans = prices[j] - prices[i]
                res = max(res, ans)
            else:
                i = j
            j += 1
        return res