class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output = []

        while matrix :
            # first reading the and popping the first list
            output+= matrix.pop(0)  # output+= adds the items instead of adding the whole list at once

            #then popping the last element of rest of the items and then adding
            if matrix and matrix[0] :
                for i in matrix :
                    output.append(i.pop())   #pop by default pops the last item

            #then reversing last element
            if matrix : 
                output += (matrix.pop()[::-1])

            #popping the first element of each item in reverse order
            if matrix and matrix[0] :
                for j in matrix[::-1] :
                    output.append(j.pop(0))



        return output
        