class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ""
        cache = ""
        for letter in s:
            if letter == " ":
                ret += self.reverse_one_word(cache) + " "
                cache = ""
            else:
                cache += letter
        ret += self.reverse_one_word(cache)
        return ret


solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))
