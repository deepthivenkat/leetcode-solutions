
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return
        reference,orig_head, head_ini = head,head,head
        while orig_head:
            temp = RandomListNode(orig_head.label)
            next_node = orig_head.next
            temp.next = next_node
            orig_head.next = temp
            orig_head = next_node
        while head_ini and head_ini.next:
            head_ini.next.random = head_ini.random.next if head_ini.random else None
            head_ini = head_ini.next.next
        ret_head = copy = reference.next
        while reference and copy:
            reference.next = reference.next.next if reference.next else None
            copy.next = copy.next.next if copy.next else None
            reference = reference.next
            copy = copy.next
        return ret_head