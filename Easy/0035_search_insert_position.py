class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Edge case: empty array — target would be inserted at index 0
        if not nums:
            return 0

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                # Found it exactly — that's the index
                return mid

            if nums[mid] < target:
                # Target is bigger than nums[mid], so it belongs
                # somewhere to the right — narrow the range
                left = mid + 1

            if nums[mid] > target:
                # Target is smaller than nums[mid], so it belongs
                # somewhere to the left — narrow the range
                right = mid - 1

        # Target was never found, so the loop exits once left
        # crosses right. At that point, left is sitting exactly
        # where the target would need to be inserted to keep
        # the array sorted.
        return left
