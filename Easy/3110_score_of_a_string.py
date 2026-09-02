class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Store the total score of the string
        sum = 0

        # Loop through each character except the last one
        for i in range(len(s) - 1):

            # Find the absolute difference between the ASCII values
            # of the current character and the next character
            # and add it to the total score
            sum = sum + abs(ord(s[i]) - ord(s[i + 1]))

        # Return the total score of the string
        return sum
