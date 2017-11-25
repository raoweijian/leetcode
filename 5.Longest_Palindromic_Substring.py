class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ""
        if len(s) < 2:
            return s

        for i in range(len(s)):
            odd = self.expand(i, i, s)
            even = self.expand(i, i + 1, s)
            if len(odd) > len(ret):
                ret = odd
            if len(even) > len(ret):
                ret = even
        return ret

    def expand(self, left, right, s):
        ret = ""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        ret = s[left + 1: right]
        return ret
