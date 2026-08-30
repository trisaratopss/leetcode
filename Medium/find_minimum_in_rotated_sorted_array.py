class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Edge case: single element is trivially the minimum
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # If the very next element drops below mid, we've
            # found the exact "seam" where the rotation breaks —
            # that next element is the minimum
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]

            # If mid itself is lower than the element before it,
            # mid is sitting right at the seam — it's the minimum
            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            # Otherwise, decide which half still contains the seam
            if nums[mid] > nums[right]:
                # Right half must contain the rotation point
                left = mid + 1
            else:
                # Left half (including mid) might contain it —
                # keep mid in play, don't exclude it
                right = mid
