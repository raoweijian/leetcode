#coding=utf8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = 0
        tmp = root
        while tmp is not None:
            length += 1
            tmp = tmp.next

        avg = length / k #平均每部分的长度
        mod = length % k #剩余没分配的数量

        #首选计算出整个链表需要在哪些部分断开
        #比如输入是 [1,2,3,4,5] k=4 时，那么分配成 [1,2], [3], [4], [5] 断点就是 [2, 3, 4, 5]
        #如果输入是 [1 - 22], k=4时，断点就是 [6, 12, 17, 22]
        break_points = []
        for i in range(k):
            if i < mod:
                break_points.append((avg + 1) * (i + 1))
            else:
                break_points.append((avg + 1) * mod + (i + 1 - mod) * avg)

        ret = []
        begin = root
        for i in range(length):
            if (i + 1) in break_points:
                #断开
                tmp = root.next #先把后续内容保存下来
                root.next = None #断开当前结点与剩下的节点
                ret.append(begin) # 存进数组

                #开始下一个节点
                root = tmp
                begin = root
            else:
                root = root.next

        # 处理 k > 链表长度的情况
        for i in range(k - len(ret)):
            ret.append(None)

        return ret
