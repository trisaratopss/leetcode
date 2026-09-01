class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """

        # Create an empty list to store the friends in their finishing order
        output = []

        # Loop through each participant in the overall finishing order
        for i in order:
            # Check if the participant is one of your friends
            if i in friends:
                # Add the friend to the output in the order they finished
                output.append(i)

        # Return the finishing order containing only your friends
        return output
