class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if len(nums) == 1:
            ret = [nums]
            return ret

        for i in range(len(nums)):
            sub_arr = nums[:i] + nums[i + 1:]
            sub_ret = self.permute(sub_arr)
            for one in sub_ret:
                ret.append([nums[i]] + one)
        return ret
