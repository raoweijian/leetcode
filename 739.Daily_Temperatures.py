class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ret = []
        cache = {}
        for index in range(len(temperatures)):
            temp = temperatures[index]
            if temp not in cache:
                cache[temp] = []
            cache[temp].append(index)

            ret.append(0)


            for process_temp in range(30, temp):
                if process_temp not in cache:
                    continue

                for process_index in cache[process_temp]:
                    ret[process_index] = index - process_index

                del cache[process_temp]
        return ret
