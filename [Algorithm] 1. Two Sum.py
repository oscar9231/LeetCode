class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_len = len(nums)
        i = list_len - 2
        n = 1
        while i < list_len - 1 and n < list_len:
            summa = nums[i] + nums[i + n]
            if summa == target:
                return [i, i + n]
            elif i + n == list_len - 1:
                i -= 1
                n = 1
            else:
                n += 1
