class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        temp = prices[0]
        res = 0
        for i in prices:
            temp = min(temp,i)
            if i - temp > res:
                res = i - temp
        return res
