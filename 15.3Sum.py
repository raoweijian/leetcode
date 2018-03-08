class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ret = []
        for i in range(n - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                target = 0 - nums[i]
                left = i + 1
                right = n - 1
                while left < right:
                    if nums[left] + nums[right] == target:
                        ret.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] > target:
                        #大了，右边的需要左移
                        right -= 1
                    else:
                        left += 1
        return ret
