class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res += list(map(lambda x: x + [i], res))
        return res
