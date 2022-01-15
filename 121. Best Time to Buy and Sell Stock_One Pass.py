# time complexity: O(n). Only a single pass is needed.
# space complexity: O(1). Only three variables are used.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = max(prices)
        max_profit = 0
        for i in range(len(prices)):
            diff = prices[i] - min_price
            if diff < 0:
                min_price = prices[i]
            elif diff > max_profit:
                max_profit = diff
        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    print(sol.maxProfit(prices))
