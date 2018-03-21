class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [nums[0]]
        for i in range(1, len(nums)):
            append = nums[i] + dp[i - 1] if dp[i - 1] > 0 else nums[i]
            dp.append(append)
        return max(dp)


"""
这道题使用了动态规划的方法。
动态规划中最重要的是找到初始问题的子问题，然后从子问题开始回溯，解决初始问题。
这里提出的子问题是 maxSubArray(nums, i + 1), 意思是 nums[:i + 1] 的最大子序列和，并且以 nums[i]结尾
所以可以推导出：
maxSubArray(sums, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) : 0 + A[i];

通过这种方法，对 0 <= i < len(nums)，都可以找到以 nums[i] 结尾的，最大子序列的和
最后再，从这一堆和当中，取出最大值即可
"""
