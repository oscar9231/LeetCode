class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums[-1])
            nums.pop()

            
# very smart way from programming pearls
# class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    # def rotate(self, nums, k):
       # n = len(nums)
       # k = k % n
       # nums[:] = nums[n-k:] + nums[:n-k]
