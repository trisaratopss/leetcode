class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Create a set to store each distinct starting character
        substring = set()

        # Loop through every character in the string
        for i in s:
            # Add the character to the set
            # Duplicate characters are automatically ignored
            substring.add(i)

        # The maximum number of substrings is equal to
        # the number of distinct characters in the string
        return len(substring)
