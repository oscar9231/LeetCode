# Dutch National Flag Problem

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        beg = cur = 0
        end = len(nums) - 1
        while cur <= end:
            if nums[cur] == 0:
                nums[beg], nums[cur] = nums[cur], nums[beg]
                beg += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[end], nums[cur] = nums[cur], nums[end]
                end -= 1
