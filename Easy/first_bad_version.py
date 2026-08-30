# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Edge case: only one version exists, it must be the
        # first bad one if we're being asked at all
        if n == 1:
            return 1

        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            if not isBadVersion(mid):
                # mid is good, so the first bad version (if any)
                # must be somewhere after it — narrow rightward
                left = mid + 1

            if isBadVersion(mid):
                # mid is bad, so it's a candidate for "first bad" —
                # but there could be an earlier bad one too, so
                # keep mid in consideration and search left of it
                right = mid - 1

        # When the loop ends, left has been pushed past every
        # good version and stopped just before crossing into
        # bad territory — landing exactly on the first bad version
        return left
