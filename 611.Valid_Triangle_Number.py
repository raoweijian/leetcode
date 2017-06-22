class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        nums = nums[::-1]

        sol = 0

        for i in range(len(nums) - 2):
            k = len(nums) - 1
            for j in range(i + 1, k):
                if j >= k:
                    break
                diff = nums[i] - nums[j]
                while nums[k] <= diff and k > j:
                    k -= 1
                sol += (k - j)
        return sol
