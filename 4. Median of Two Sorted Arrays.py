class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sort_list = sorted(nums1 + nums2)
        if len(sort_list) % 2 == 1:
            return sort_list[int((len(sort_list) - 1 ) / 2)]
        else:
            return (sort_list[int(len(sort_list)/2)] + sort_list[int(len(sort_list) / 2 - 1)]) / 2.0
