class Solution:
    """
    解题的思路挺简单
    我们只需要把所有的 x 都合并到同一项里，所有的常数合并到另一个项里，最后用常数除以 x 的系数即可
    比如一个式子: x+5-3+x=6+x-2
    左边合并为 2x + 2, 右边合并为 x + 4
    再把右边移到左边来，得到 x - 2 = 0

    问题的关键在于怎么进行这个合并的操作

    这个答案里用了两个成员变量来存储 x 的系数和常数的值，然后遍历这个等式，每遇到一个 x 项，就修改一下 x 的系数；
    每遇到一个常数项，就修改常数的值。
    需要注意的是，我们都知道，把等号右边的项移到左边，需要把符号变一下。所以用了另一个变量来记录当前是否遍历到了
    等号右边。
    """
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        self.coe_x = 0
        self.consis = 0

        global_negtive = 1 # 用于区分等号左边和右边的项
        tmp_negtive = 1 # 当前处理的这个项的符号
        tmp = ""
        for letter in equation:
            if letter == '-':
                self._jiesuan(tmp, tmp_negtive * global_negtive)
                tmp_negtive = -1
                tmp = ""
            elif letter == '+':
                self._jiesuan(tmp, tmp_negtive * global_negtive)
                tmp_negtive = 1
                tmp = ""
            elif letter == '=':
                self._jiesuan(tmp, tmp_negtive * global_negtive)
                global_negtive = -1
                tmp_negtive = 1
                tmp = ""
            else:
                tmp += letter
        self._jiesuan(tmp, tmp_negtive * global_negtive)

        if self.coe_x == 0:
            if self.consis == 0:
                return 'Infinite solutions'
            else:
                return 'No solution'
        else:
            x = int(-self.consis / self.coe_x)
            return "x=%s" % x

    def _jiesuan(self, tmp, negtive):
        if len(tmp) == 0:
            return
        if 'x' in tmp:
            tmp = tmp.rstrip('x')
            if tmp == '':
                num = 1
            elif tmp == '-':
                num = -1
            else:
                num = int(tmp)
            self.coe_x += num * negtive
        else:
            num = int(tmp)
            self.consis += num * negtive
