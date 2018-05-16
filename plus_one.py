class Solution(object):
    def plusOne(self, head):
        number = []
        head_copy = head
        while head_copy:
            number.append(head_copy.val)
            head_copy = head_copy.next
        number = str(int("".join(map(str,number)))+1)
        number = number[::-1]
        prev = None
        for num in number:
            head = ListNode(num)
            head.next = prev
            prev = head
        return prev