class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [[1]]
        for i in range(1, rowIndex + 1):
            res.append(list(map(lambda x, y: x + y, [0] + res[-1], res[-1] + [0])))
        return res[-1]
