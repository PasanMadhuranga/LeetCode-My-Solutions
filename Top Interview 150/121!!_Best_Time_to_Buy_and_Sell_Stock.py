class Solution(object):
    def maxProfit(self, prices):
        """
        This function finds the maximum profit from buying and selling a stock.

        :type prices: List[int]
        :rtype: int
        """

        # 'left' is the buy day and 'right' is the sell day.
        left = 0
        right = 1

        # Initialize maxProfit to 0, as initially, no profit has been made.
        maxProfit = 0

        # Loop through the prices while the sell day is within the list.
        while (right < len(prices)):
            # Calculate current profit by subtracting the buy price from the sell price.
            currProfit = prices[right] - prices[left]

            # If current profit is positive, update maxProfit if current profit is greater.
            if (currProfit > 0):
                maxProfit = max(currProfit, maxProfit)
            else: 
                # If current profit is negative or zero, move the buy day to the sell day.
                # This is because we want to buy at a lower price to increase potential profit.
                left = right

            # Move to the next sell day.
            right += 1
        
        # Return the maximum profit found.
        return maxProfit



# Another solution using Kadane's Algorithm.
# class Solution {
#     public int maxProfit(int[] prices) {
#         // maxCur keeps track of the current running profit.
#         int maxCur = 0;

#         // maxSoFar keeps track of the maximum profit found so far.
#         int maxSoFar = 0;

#         // Start iterating from the second element in the array.
#         for(int i = 1; i < prices.length; i++) {
#             // Update maxCur. It's the maximum of 0 and the sum of maxCur and 
#             // the difference between the current price and the previous price.
#             // This effectively calculates the profit or loss if the stock bought 
#             // on the previous day (i-1) was sold on the current day (i).
#             maxCur = Math.max(0, maxCur += prices[i] - prices[i-1]);

#             // Update maxSoFar if maxCur is greater than maxSoFar.
#             // This keeps track of the highest profit found so far.
#             maxSoFar = Math.max(maxCur, maxSoFar);
#         }

#         // Return the maximum profit that can be made.
#         return maxSoFar;
#     }
# }
