class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a == 1:
            return 1

        factors = [9,8,7,6,5,4,3,2]
        chosen = []
        while 1:
            done = 0
            for factor in factors:
                #可以整除
                if a % factor == 0:
                    chosen.append(factor)
                    a = a / factor
                    done = 1
                    break
            if done == 0:
                break
        if a != 1:
            return 0

        else:
            chosen.sort()
            ret = 0
            index = 0
            length = len(chosen)
            for dig in chosen:
                e = length - index - 1
                ret += dig * 10 ** e
                index += 1
                if ret >= 1073741824:
                    ret = 0
                    break
            return ret
