class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                # Found it
                return mid

            # <= (not <) matters here: when left == mid (a
            # single-element left side), it must still count as
            # "sorted" so we route into the correct branch
            if nums[left] <= nums[mid]:
                # Left half [left..mid] is sorted normally
                if nums[left] <= target and nums[mid] > target:
                    # target falls inside this sorted left range —
                    # search there
                    right = mid - 1
                else:
                    # target must be in the other half
                    left = mid + 1
            else:
                # Right half [mid..right] is sorted normally
                # (since left half wasn't)
                if nums[mid] < target and target <= nums[right]:
                    # target falls inside this sorted right range —
                    # search there
                    left = mid + 1
                else:
                    # target must be in the other half
                    right = mid - 1

        # Loop exited without finding target — it isn't in nums
        return -1
