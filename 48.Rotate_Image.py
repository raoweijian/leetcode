class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        if size <= 1:
            return

        for depth in range(0, size / 2 + 1):
            top = matrix[depth][depth:size - depth]
            bottom = matrix[size - depth - 1][depth:size - depth:][::-1]
            right = []
            left = []
            for i in range(depth, size - depth):
                right.append(matrix[i][size - depth - 1])
                left.append(matrix[size - i - 1][depth])
            combine = top + right[1:] + bottom[1:] + left[1:-1]
            combine = self.move(combine, size - 1 - depth * 2)

            width = size - depth * 2
            top = combine[:width]
            right = combine[width - 1:width * 2 - 1]
            bottom = combine[width * 2 - 2:width * 3 - 2][::-1]
            left = combine[width * 3 - 3:]
            if len(left) < len(top):
                left += combine[:1]

            #还原
            matrix[depth][depth:size - depth] = top
            matrix[size - depth - 1][depth:size - depth:] = bottom
            count = 0
            for i in range(depth, size - depth):
                matrix[i][size - depth - 1] = right[count]
                matrix[size - i - 1][depth] = left[count]
                count += 1

    def move(self, arr, step):
        size = len(arr)
        return arr[size - step:] + arr[:size - step]
