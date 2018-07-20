class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        len_biglist = len(A)
        len_smalllist = len(A[0])
        i = 0
        while i < len_biglist:
            j = 0
            while j < len_smalllist // 2:
                if A[i][j] == A[i][len_smalllist - 1 - j]:
                    if A[i][j] == 1:
                        A[i][j] = 0
                        A[i][len_smalllist - 1 - j] = 0
                    else:
                        A[i][j] = 1
                        A[i][len_smalllist - 1 - j] = 1
                j += 1
            i += 1
        if len_smalllist % 2 == 1:
            for item in A:
                if item[len_smalllist // 2] == 0:
                    item[len_smalllist // 2] = 1
                else:
                    item[len_smalllist // 2] = 0
        return A
