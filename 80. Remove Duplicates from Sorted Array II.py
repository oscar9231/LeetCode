class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        length = len(nums) - 1
        while i < length:
            if nums[i] != nums[i+1]:
                i += 1
            elif nums[i] == nums[i+1]:
                if i+2 <= length and nums[i] == nums[i+2]:
                    nums.remove(nums[i])
                    length -= 1
                else:
                    i += 2
        return len(nums)
