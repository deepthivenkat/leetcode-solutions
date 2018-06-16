# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    @staticmethod
    def iter_ll(head):
        res = []
        while head:
            for node in head.left,head.right:
                if node:
                    yield node
            head = head.next
    def connect(self, root):
        node = root
        while node:
            first_node = None
            for n in Solution.iter_ll(node):
                if not first_node:
                    first_node =cur= n
                else:
                    cur.next = cur=n
            node = first_node  