class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        i = 0
        j = len(height) - 1
        while i < j:
            h = min(height[i], height[j])
            ret = max(ret, (j - i) * h)
            while height[i] <= h and i < j:
                i += 1
            while height[j] <= h and i < j:
                j -= 1
        return ret
