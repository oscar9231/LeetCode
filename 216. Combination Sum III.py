class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        self.sum_help(k, n, 1, [], res)
        return res

    def sum_help(self, k, n, curr, arr, res, curr_sum=0):
        if len(arr) == k:
            if curr_sum == n:
                res.append(arr[:])
            return
        if curr_sum >= n:
            return

        for i in xrange(curr, 10):
            arr.append(i)
            self.sum_help(k, n, i + 1, arr, res, curr_sum + i)
            arr.pop()

# still do not understand
