# time complexity: O(n^2). Loop runs (n(n-1))/2 times
# space complexity: O(1). Only a variables is used

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    max_profit = max(max_profit, prices[j]-prices[i])
        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    print(sol.maxProfit(prices))
