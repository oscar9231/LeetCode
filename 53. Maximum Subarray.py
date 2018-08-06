#Kadane Algorithm

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        current_sum = max_sum = nums[0]
        for i in nums[1:]:
            current_sum = max(i, current_sum + i)
            max_sum = max(max_sum, current_sum)
        return max_sum
