class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        current, res = float('-inf'), 0
        for pair in sorted(pairs, key=lambda x: x[1]):
            if current < pair[0]:
                current, res = pair[1], res + 1
        return res
