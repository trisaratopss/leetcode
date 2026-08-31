class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Calculate the total sum of all numbers in the array
        sum = 0
        for i in nums:
            sum += i

        # Find the remainder when the sum is divided by k.
        # Since each operation decreases the array sum by 1,
        # we need to decrease the sum by exactly this remainder
        # to reach the nearest smaller multiple of k.
        return sum % k
