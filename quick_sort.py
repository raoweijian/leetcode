# coding=utf-8

import random
import time


def quick_sort(arr, left, right):
    if left >= right:
        return
    mid = part(arr, left, right)

    # 这里 mid -1, mid + 1，是因为 arr[mid] 这个元素的位置已经确定是正确的了，所以不需要再对它进行排序，减少计算量
    quick_sort(arr, left, mid - 1)
    quick_sort(arr, mid + 1, right)


def part(arr, left, right):
    target = arr[left]

    while left < right:
        # 从右边开始搜索，找到一个小于 target 的
        while left < right and arr[right] >= target:
            right -= 1
        # 把找到的这个值放到 left 的位置
        arr[left] = arr[right]
        # 试想一下，如果已经排好序了，left = 0, right = length - 1
        # 那么 right 会一直减到 0，此时执行 arr[left] = arr[right] 实际上是数组没有发生变化

        # 从左边开始搜索，找到一个大于 target 的
        while left < right and arr[left] < target:
            left += 1
        # 把找到的值放到 right 的位置
        arr[right] = arr[left]

        # 这里再想一下，如果本次循环中，left 一直加到 = right, right 已经发生了一次替换 比如这一轮开始时，数组长这样: target = 4
        #                           [4, 1, 2, 3, 3, 5, 6, 7]
        # right 交换一次之后，变成这样:
        #                           [3, 1, 2, 3, 3, 5, 6, 7]
        # left, right 所在位置:      ↑           ↑
        # left 往右搜索到这个位置:               ↑
        # 此时 left 和 right 重叠, 发生一次交换，实际数组仍然没有变化

    # 这里把 target 放到 left位置是出于习惯。实际上上面的循环结束之后，left 一定和 right 相等的。用 left 或者 right 都是可以的
    arr[right] = target
    return left


print("构造数据中")
a = []
start = time.time()
size = 10000
for i in range(size):
    a.append(random.randint(0, 20))
end = time.time()
print("构造数据完成, 用时: %d, 数据长度: %d" % (end - start, len(a)))

print("排序开始...")
start = time.time()
quick_sort(a, 0, len(a) - 1)
end = time.time()
print("排序完成， 用时 %.3f s" % (end - start))


if sorted(a) == a:
    print("sort done!")
else:
    print("sort fail!")
