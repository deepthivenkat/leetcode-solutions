class Solution(object):
    def addTwoNumbers(self, l1, l2):
        add_lists = l1,l2
        carry=0
        dummy=front_end = ListNode(0)
        while add_lists or carry:
            carry += sum(l.val for l in add_lists)
            add_lists = [l.next for l in add_lists if l.next]
            front_end.next=front_end=ListNode(carry%10)
            carry/=10
        return dummy.next