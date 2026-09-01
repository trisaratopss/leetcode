class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Create an empty list to store the new permutation
        output = []

        # Loop through every index in nums
        for i in range(len(nums)):
            # Use nums[i] as an index into nums,
            # then add that value to the output array
            output.append(nums[nums[i]])

        # Return the completed array
        return output
