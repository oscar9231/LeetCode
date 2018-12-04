#python3

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        width = j - i
        res = min(height[i], height[j]) * width
        while width > 1:
            if height[i] >= height[j]:
                j -= 1
                width -= 1
            else:
                i += 1
                width -= 1
            res = max(res, min(height[i], height[j]) * width)
        return res
