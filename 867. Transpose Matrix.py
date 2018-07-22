class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        result = []
        while i < len(A[0]):
            j = 0
            item = []
            while j < len(A):
                item.append(A[j][i])
                j += 1
            result.append(item)
            i += 1
        return result
