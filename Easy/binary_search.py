class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Edge case: empty array can never contain the target
        if not nums:
            return -1

        # Boundaries of the current search space —
        # target could still be anywhere in [left, right]
        left = 0
        right = len(nums) - 1

        while left <= right:
            # Midpoint of the current range — our guess
            mid = (right + left) // 2

            if nums[mid] == target:
                # Found it
                return mid

            if nums[mid] < target:
                # Target must be larger than nums[mid], so it can
                # only be to the right — shrink the range by
                # excluding mid and everything before it
                left = mid + 1

            if nums[mid] > target:
                # Target must be smaller than nums[mid], so it can
                # only be to the left — shrink the range by
                # excluding mid and everything after it
                right = mid - 1

        # Loop ended without finding it — left has crossed right,
        # meaning the search space is empty
        return -1