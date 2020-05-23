class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        record = {}

        for l in t:
            t_count[l] = t_count.get(l, 0) + 1

        l = 0
        r = -1

        cur_len = len(s) + 1
        ret_l = -1
        ret_r = -1

        print(t_count)
        while r < len(s):
            r += 1
            if r < len(s) and s[r] in t_count:
                record[s[r]] = record.get(s[r], 0) + 1

            print(record, l, r)
            while self.check(t_count, record) and l <= r:
                print("check pass: " + str(record))
                if r - l + 1 < cur_len:
                    cur_len = r - l + 1
                    ret_l = l
                    ret_r = r

                record[s[l]] = record.get(s[l], 0) - 1

                l += 1

        if ret_l != -1:
            return s[ret_l : ret_r + 1]
        else:
            return ""



    def check(self, a, b):
        for l in a:
            if l not in b or b[l] < a[l]:
                return False
        return True


s = Solution()
print(s.minWindow("a", "aa"))
