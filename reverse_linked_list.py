class Solution(object):
    def reverseList(self, head):
        c = head
        length =0
        while c:
            length+=1
            c = c.next
        def swap_nodes(head, i, n):
            first,last = head,head
            start,end = i, n-i-1
            while start >0:
                first = first.next
                start -=1
            while end>0:
                last = last.next
                end -= 1
            first.val,last.val=last.val,first.val
        for i in range(length//2):
            swap_nodes(head, i, length)
        return head