class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i in range(len(nums)):
            # The value that would complete the pair to reach target
            needed = target - nums[i]

            # If we've already seen it, we found our pair
            # return its index and the current index
            if needed in seen:
                return [i, seen[needed]]

            # Otherwise, record this number so future iterations
            # can check against it
            seen[nums[i]] = i
