# clear explanation: https://blog.csdn.net/ebowtang/article/details/50448037
# MIT explanation: http://courses.csail.mit.edu/6.006/spring11/lectures/lec02.pdf

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return high
