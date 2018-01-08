class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cash = [0] * 10001
        for num in nums:
            cash[num] += num
        return self.rob(cash)

    def rob(self, nums):
        prev = 0
        curr = 0
        for num in nums:
            prev, curr = curr, max(prev + num, curr)
        return curr
