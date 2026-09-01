class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # Create an empty list to store the degree of each vertex
        list = []
        
        # Loop through each row in the adjacency matrix
        for i in matrix:
            # Sum the row to find the degree of the vertex
            # and add it to the list
            list.append(sum(i))

        # Return the list containing the degree of each vertex
        return list
