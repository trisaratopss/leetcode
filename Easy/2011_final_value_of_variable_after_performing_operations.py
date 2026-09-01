class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        
        # Initialize X to 0
        i = 0 

        # Loop through each operation in the array
        for j in range(len(operations)):

            # If the operation contains "+", increment X by 1
            if "+" in operations[j]:
                i += 1

            # Otherwise, the operation contains "-", so decrement X by 1
            else:
                i -= 1
        
        # Return the final value of X after all operations
        return i
