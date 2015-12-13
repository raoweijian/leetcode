#!/usr/bin/env python
#coding=utf-8
import math

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        exist = {}  # 分值即长度
        max_length = 1
        for n in nums:
            length = 1
            left = 0  # n 左边的长度
            right = 0 # n 右边的长度
            if n in exist:
                continue

            if n - 1 in exist:
                length += exist[n - 1]
                left = exist[n - 1]
            if n + 1 in exist:
                length += exist[n + 1]
                right = exist[n + 1]
            
            # 更新左右的长度
            exist[n - left] = length
            exist[n] = length
            exist[n + right] = length

            if max_length < length:
                max_length = length
        return max_length

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

    def countPrimes(self, n):
        if n <= 2:
            return 0
        ret = 0
        limit = int(math.sqrt(n))
        
        a = [False, False]
        for i in range(2, n + 1):
            a.append(True)
        
        for i in range(2, limit + 1):
            if a[i]:
                j = i;
                while j * i <= n:
                    a[j * i] = False
                    j += 1
        
        for i in range(2, n):
            if a[i]:
                ret += 1
        
        return ret
    
    def reverseList(self, head):
        """
        206 Reverse Linked List
        """
        if head == None or head.next == None:
            return head
        
        current = head.next
        previous = head
        tmp = None
        head.next = None
        while current.next != None:
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp
        current.next = previous
        return current

    def canWinNim(self, n):
        """
        292
        如果有4个，就是肯定输。如果有5 - 7个，就肯定赢。那么如果有8个呢？
        你取1-3个，就给对手留下5-7个，那么就是你输了。
        如果总共15个石头，你就拿走3个，还剩12个。无论他拿走几个，你都可以让他再面对8个，以此类推。

        所以可以得出，谁面对4个的倍数，那么下次还可以让他面对4个的倍数。所以输定了
        """
        if n % 4 == 0:
            return False
        else:
            return True


    def singleNumber(self, nums):
        """
        262
        两个数只出现一次，那么这两个数的二进制形式一定在某一位不一致。
        假设在 i 位不一致，那么我们把在 i 位为1的分为A组，在i位为0的分为B组；而我们要找的这两个数字，一个位于A组，一个位于B组。
        对于两个一样的数字，那么它们一定被分在同一组。
        现在我们可以得到 A、B两组都是由成对出现的数字和一个单独的数字构成。
        而两个相同的数字，取异或，结果为0。
        所以可以得到 A 组中，要找的数字为把A组所有数字异或，B组也一样。
        """
        x = nums[0]
        for i in range(1, len(nums)):
            x = x ^ nums[i]
        
        marker = 1
        for i in range(len(nums)):
            if marker & x != marker:
                marker = marker << 1
            else:
                break
        
        result_x = 0
        result_y = 0
        for i in range(len(nums)):
            if nums[i] & marker:
                # nums[i] 在 marker 位上为 1, 属于左半部分
                result_x = result_x ^ nums[i]  # 异或操作，成对的duplicate会抵消
            else:
                result_y = result_y ^ nums[i]
        return (result_x, result_y)

    def maxProfit(self, prices):
        """
        Best Time to Buy and Sell Stock II
        简单来说，如果明天的价格比今天高，那么就今天买，明天卖。否则就不操作
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

class Queue(object):
    """
    232 Implement Queue using Stacks
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        ret = self.stack[0]
        self.stack = self.stack[1:]
        return ret

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]


    def empty(self):
        """
        :rtype: bool
        """
        return True if len(self.stack) == 0 else False

solution = Solution()

print solution.canWinNim(8)
