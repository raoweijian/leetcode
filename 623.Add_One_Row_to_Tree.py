# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: Node
        :type v: int
        :type d: int
        :rtype: Node
        """

        if d == 1:
            tmp = root
            root = TreeNode(v)
            root.left = tmp
            return root

        depth = 1
        nodes = [root]
        while depth <= d - 2:
            new_nodes = []
            for node in nodes:
                if node.left is not None:
                    new_nodes.append(node.left)
                if node.right is not None:
                    new_nodes.append(node.right)
            nodes = new_nodes
            depth += 1

        for node in nodes:
            if node.left is not None:
                tmp = node.left
                node.left = TreeNode(v)
                node.left.left = tmp
            else:
                node.left = TreeNode(v)

            if node.right is not None:
                tmp = node.right
                node.right = TreeNode(v)
                node.right.right = tmp
            else:
                node.right = TreeNode(v)
        return root
