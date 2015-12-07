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

print solution.countPrimes(1500000)
