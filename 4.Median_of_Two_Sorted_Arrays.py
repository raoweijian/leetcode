class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(A)
        n = len(B)
        if m > n:
            m, n, A, B = n, m, B, A

        imin, imax, left_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = left_len - i
            if i < m and B[j - 1] > A[i]:
                #i太小了，需要增大i
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                #i 太大了，需要减小
                imax = i - 1
            else:
                #i is perfect
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                #由于我们上面定义 left_len 的方式，如果 m + n 是奇数的话
                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])
                return (max_of_left + min_of_right) / 2.0
