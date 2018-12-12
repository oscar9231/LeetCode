#DP

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return None
        i = len(triangle)
        for row in range(1, i):
            triangle[row][0] += triangle[row - 1][0]
            triangle[row][-1] += triangle[row - 1][-1]
        for row in range(2, i):
            j = len(triangle[row])
            for column in range(1, j - 1):
                triangle[row][column] += min(triangle[row - 1][column - 1], triangle[row - 1][column])
        return min(triangle[-1])
