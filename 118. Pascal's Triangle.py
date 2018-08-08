class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1, numRows):
            res.append(list(map(lambda x, y: x + y, [0] + res[-1], res[-1] + [0])))
        return res[:numRows]
