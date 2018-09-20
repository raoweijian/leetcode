class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []

        def helper(cur, digits, index, m, ret):
            if len(cur) == len(digits):
                ret.append(cur)
            else:
                for letter in m[digits[index]]:
                    helper(cur + letter, digits, index + 1, m, ret)

        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ret = []
        cur = ""
        helper(cur, digits, 0, m, ret)
        return ret
