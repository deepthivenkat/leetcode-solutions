class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        cycle_present = False
        fast,slow = head,head
        while fast and slow:
            slow = slow.next
            fast = fast.next.next if fast and fast.next else None
            if fast and fast == slow:
                cycle_present = True
                break
        if not cycle_present:
            return None
        while head!=slow:
            head = head.next
            slow = slow.next
        return head