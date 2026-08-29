class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Lowest price seen so far — the best possible "buy" point
        # up to the current day
        min = prices[0]

        # Best profit found so far, assuming we sell at some day
        # after buying at the lowest price seen before it
        max = 0

        for i in range(0, len(prices)):
            # Update our running minimum — if today's price is
            # lower than anything before it, this becomes our
            # new best "buy" price for future days
            if prices[i] < min:
                min = prices[i]

            # Check: if we sold today, using the best "buy" price
            # so far, would that beat our current best profit?
            if (prices[i] - min) > max:
                max = prices[i] - min

        return max