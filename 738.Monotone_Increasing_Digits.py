import time

class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        while not self.is_monotone(N):
            #print("processing %d" % N)
            #time.sleep(1)
            n_str_arr = list(str(N))
            prev = 0
            for i in range(len(n_str_arr)):
                num = int(n_str_arr[i])
                if num < prev:
                    #print("befor: " + "\t".join(n_str_arr))
                    n_str_arr[i - 1] = str(prev - 1)
                    #print("after: " + "\t".join(n_str_arr))
                    for j in range(i, len(n_str_arr)):
                        n_str_arr[j] = "9"
                    #print("after: " + "\t".join(n_str_arr))
                    break
                prev = num
            N = int("".join(n_str_arr))
        return N

    def is_monotone(self, N):
        n_str = str(N)
        prev = "0"
        for letter in n_str:
            if int(letter) < int(prev):
                return False
            prev = letter
        return True
