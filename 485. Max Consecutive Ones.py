class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        length = 0
        for num in nums:
            if num == 1:
                stack.append(num)
            else:
                stack = []
            if len(stack) > length:
                length = len(stack)
        return length
