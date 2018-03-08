import time

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mid = n / 2
        edge_left = 0
        edge_right = n - 1
        while mid != 0 and mid < n:
            left = sum(nums[:mid])
            right = sum(nums[mid + 1:])
            print("mid: %d, left: %d, right: %d" % (mid, left, right))
            if left == right:
                return mid
            elif left < right:
                edge_left, mid = mid, (edge_right + mid) / 2
            else:
                edge_right, mid = mid, (edge_left + mid) / 2
            time.sleep(0.5)
        return -1




solution = Solution()
nums = range(13)
print(solution.pivotIndex(nums))
