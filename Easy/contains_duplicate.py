class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Set to track numbers we've already encountered
        num_set = set()

        for i in range(0, len(nums)):
            # If we've seen this number before, we found
            # our duplicate — return immediately, no need
            # to check the rest of the array
            if nums[i] in num_set:
                return True

            # Otherwise, record it so future iterations
            # can check against it
            num_set.add(nums[i])

        # Made it through the whole array with no repeats found
        return False