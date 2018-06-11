class Solution(object):
    def swap_given_top(self,node):
        node.val,node.next.val = node.next.val,node.val
        return
        
    def swapPairs(self, head):
        return_pointer = head
        while head and head.next:
            self.swap_given_top(head)
            head = head.next.next
        return return_pointer
        """
        :type head: ListNode
        :rtype: ListNode
        """