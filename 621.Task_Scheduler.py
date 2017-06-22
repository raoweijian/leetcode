class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        record = {}
        for letter in tasks:
            if letter not in record:
                record[letter] = 1
            else:
                record[letter] += 1

        sort = sorted(record.iteritems(), key = lambda d:d[1], reverse = True)
        max_num = sort[0][1]
        ret = (n + 1) * (max_num - 1)
        for letter in record:
            if record[letter] == max_num:
                ret += 1
        return max(len(tasks), ret)
