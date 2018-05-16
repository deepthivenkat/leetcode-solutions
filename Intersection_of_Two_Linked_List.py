class Solution(object):
    def getIntersectionNode(self, headA, headB):
        count_A,count_B = 0,0
        cpy_A,cpy_B = headA, headB
        while cpy_A:
            count_A +=1
            cpy_A = cpy_A.next
        while cpy_B:
            count_B+=1
            cpy_B = cpy_B.next
        diff = abs(count_A-count_B)
        if count_A > count_B:
            l1= headA
            l2=headB
        else:
            l1= headB
            l2=headA
        while diff:
            l1 = l1.next
            diff -=1
        while l1 and l2:
            if l1==l2:
                return l1
            l1,l2=l1.next,l2.next
        return None
            