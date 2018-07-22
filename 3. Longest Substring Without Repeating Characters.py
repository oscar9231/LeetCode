class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_1 = ""
        j = 0
        lengsub = 1
        if s == "":
            return 0
        else:
            while j < len(s):
                i = j
                while i < len(s):
                    if s[i] not in str_1:
                        str_1 += s[i]
                    else:
                        if len(str_1) >= lengsub:
                            lengsub = len(str_1)
                            str_1 = ""
                        else:
                            str_1 = ""
                        break
                    i += 1
                j += 1
            return lengsub
