class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """

        # Create an empty list to store the indices of
        # words that contain the character x
        list = []

        # Loop through every index in the words list
        for i in range(len(words)):

            # Check if the character x appears anywhere
            # in the word at the current index
            if x in words[i]:

                # If x is found, add the index of that word
                # to the result list
                list.append(i)

        # Return all indices whose words contained x
        return list
