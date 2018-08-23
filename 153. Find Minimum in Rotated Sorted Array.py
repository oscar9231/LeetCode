# Time complexity: O(n)

class Solution():
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    return min(nums)
    


# binary search, Time complexity: O(logN)
class Solution():
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, last = 0, len(nums) - 1
        while first < last:
            midpoint = (first + last) // 2
            print(midpoint)
            if nums[midpoint] > nums[last]:
                first = midpoint + 1
            else:
                last = midpoint
        return nums[first]
