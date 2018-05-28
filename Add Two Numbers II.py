class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s1,s2 = [],[]
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2= l2.next
        carry = 0
        dummy = current = ListNode(0)
        while s1 or s2 or carry:
            carry += s1.pop() if s1 else 0 
            carry += s2.pop() if s2 else 0
            current.val += carry%10
            head = ListNode(0)
            carry /= 10
            head.next = current
            current = head
        return current if current.val else current.next