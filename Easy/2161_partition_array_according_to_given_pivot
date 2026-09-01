class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """

        # Create separate lists for elements greater than,
        # less than, and equal to the pivot
        greater = []
        less = []
        mid = []

        # Loop through each number in nums
        for i in nums:
            # Add numbers greater than the pivot to greater
            if i > pivot:
                greater.append(i)

            # Add numbers less than the pivot to less
            elif i < pivot:
                less.append(i)

            # Add numbers equal to the pivot to mid
            else:
                mid.append(i)

        # Combine the lists so smaller elements come first,
        # followed by the pivot elements, then larger elements
        return less + mid + greater
