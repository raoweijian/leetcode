class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        #整体思路比较简单，就是观察规律
        #比如 0, 1 换算成二进制都只有一位数
        # 2, 3 则是2位数
        # 4，5，6，7 是三位数，且最高位固定是1，剩余两位变化的规律与 0 - 3 是一样的
        # 8 - 15 是四位数,最高位固定是1，剩余三位的变化规律与 0 - 7 是一样的。这样就可以利用这种相对关系，计算出每个数里有多少 1
        ret = []
        idx = 2
        for i in range(num + 1):
            if i == 0:
                ret.append(0)
            elif i == 1:
                ret.append(1)
            else:
                if i == idx:
                    ret.append(1)
                    idx = idx * 2
                else:
                    ret.append(ret[i - idx] + 1)
        return ret
