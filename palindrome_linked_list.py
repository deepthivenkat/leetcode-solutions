class Solution(object):
    def get_length(self, node):
        count=0
        while node:
            count += 1
            node = node.next
        return count
    
    def reverse_ll(self,head, n):
        prev = None
        while n>0:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            n-=1
        return prev
            
            
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        head_copy = head
        length = self.get_length(head_copy)
        mid = length//2
        while mid >0:
            mid_node = head_copy
            head_copy = head_copy.next
            mid -= 1
        mid = length//2
        if length%2 !=0:
            second_head = mid_node.next.next
        else:
            second_head = mid_node.next
        rev_head = self.reverse_ll(head,mid) 
        while rev_head and second_head:
            if rev_head.val != second_head.val:
                return False
            rev_head = rev_head.next
            second_head = second_head.next
            
        return True
            
  