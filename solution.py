#!/usr/bin/env python
#coding=utf-8

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

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
    
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.

    def next(self):
        """
        :rtype: int
        """
    
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peek():
            return True
        else:
            return False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

solution = Solution()
a = [1,2,0,1]
print solution.longestConsecutive(a)
