class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for index in range(len(s)):
            ret += self.expand(s, index, index)  # 以当前索引为中心，长度为奇数的回文字符串数量
            ret += self.expand(s, index, index + 1) # 以当前索引为中心，长度为偶数的会问字符串数量
        return ret


    def expand(self, s, left, right):
        ret = 0
        while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
            ret += 1
            left -= 1
            right += 1
        return ret
