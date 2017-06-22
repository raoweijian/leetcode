class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        mins = {}
        maxs = {}

        index = 0
        for array in arrays:
            self.add_to_dict(mins, array[0], index)
            self.add_to_dict(maxs, array[-1], index)
            index += 1

        max_t = max(maxs)
        min_t = min(mins)

        if maxs[max_t] != mins[min_t] or len(maxs[max_t]) != 1:
            return max_t - min_t
        else:
            del maxs[max_t]
            del mins[min_t]
            max_r = max(maxs)
            min_r = min(mins)
            return max([max_t - min_r, max_r - min_t])

    def add_to_dict(self, target, key, index):
        if key in target:
            target[key].append(index)
        else:
            target[key] = [index]
