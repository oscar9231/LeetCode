class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        result = []
        B = []
        length_nums = len(nums)
        length_item = len(nums[0])
        if length_item * length_nums == r * c:
            for item in nums:
                for value in item:
                    B.append(value)
            i = 0
            while i < len(B):
                result.append(B[i:i+c])
                i += c
            return result
        return nums
