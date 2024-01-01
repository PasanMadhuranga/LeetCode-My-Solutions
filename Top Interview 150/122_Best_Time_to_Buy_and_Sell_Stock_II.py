class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # maxCurr represents the maximum profit that can be earned by buying on one day and selling on the next.
        # maxSoFar is the cumulative profit up to the current day.
        maxCurr = 0
        maxSoFar = 0

        # n stores the length of the prices array.
        n = len(prices)

        # Loop through each day, starting from the second day (since we compare with the previous day).
        for i in range(1, n):
            # Calculate the profit for the current day by subtracting the previous day's price from the current day's price.
            # We use max(0, ...) to ensure that maxCurr is never negative; we do not consider losses, only gains.
            maxCurr = max(0, prices[i] - prices[i-1])

            # Add the maximum profit of the current day to the cumulative profit.
            maxSoFar += maxCurr

        # Return the total maximum profit that can be achieved.
        return maxSoFar
