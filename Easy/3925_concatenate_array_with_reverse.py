class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Store the original length of nums before adding new elements
        n = len(nums)
        
        # Loop through each element in the original array
        for i in range(n):
            # Access the elements from the end of the original array
            # and append them to nums in reverse order
            nums.append(nums[n - i - 1])

        # Return nums containing the original array
        # followed by its reverse
        return nums
