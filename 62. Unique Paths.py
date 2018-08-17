#动态规划的思想

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mtx = [ [1 for i in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                mtx[i][j] = mtx[i-1][j] + mtx[i][j-1]
        return mtx[-1][-1]
