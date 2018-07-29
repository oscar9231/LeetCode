# Time limit exceeded

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        nums = list(set(nums))
        for i in range(1, length + 1):
            if i in nums:
                nums.pop(nums.index(i))
            else:
                nums.append(i)
        return nums
    

#Copy from others

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums)+1)) - set(nums))
