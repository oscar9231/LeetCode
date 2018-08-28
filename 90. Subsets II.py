class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        distict_res = []
        for i in nums:
            res += list(map(lambda x: x + [i], res))
            print(res)
        for i in res:
            if i not in distict_res:
                distict_res += [i]
        return distict_res
