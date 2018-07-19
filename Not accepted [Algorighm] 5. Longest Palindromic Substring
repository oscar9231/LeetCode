class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        longest = ""
        if s[:] == s[::-1]:
            return s
        s_reverse = s[::-1]
        i = 0
        while i < len(s):
            j = len(s)
            while j > i + 1:
                if s[i:j] in s_reverse:
                    if len(s[i:j]) >= len(longest):
                        longest = s[i:j]
                else:
                    return s[0]
                j -= 1
            i += 1
        return longest
