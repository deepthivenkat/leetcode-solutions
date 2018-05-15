class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry=0
        prev =dummy = ListNode(-1)
        while l1 and l2:
            current = l1.val+l2.val+carry
            if current >= 10: 
                carry = 1
                current = current%10
            else: carry=0
            current_node = ListNode(current)
            prev.next = current_node
            prev = current_node
            l1 = l1.next
            l2 = l2.next
        while l1:
            current = l1.val+carry
            if current >= 10: 
                carry = 1
                current = current%10
            else: carry=0
            current_node = ListNode(current)
            prev.next = current_node
            prev = current_node
            l1 = l1.next
        while l2:
            current = l2.val+carry
            if current >= 10: 
                carry = 1
                current = current%10
            else: carry=0
            current_node = ListNode(current)
            prev.next = current_node
            prev = current_node
            l2 = l2.next
        if carry:
            current_node = ListNode(carry)
            prev.next = current_node
        return dummy.next
            