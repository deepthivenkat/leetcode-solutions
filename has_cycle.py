class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        fast,slow = head,head
        while fast and slow:
            slow = slow.next
            fast = fast.next.next if fast and fast.next else None
            if fast == slow:
                return True
        return False