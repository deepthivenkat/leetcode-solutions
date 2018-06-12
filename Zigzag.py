class Solution(object):
    def zigzagLevelOrder(self, root):
        result_return,result,curr,child = [],[],[root],[]
        while curr or child:
            while curr:   
                temp = curr.pop()
                if temp:
                    result.append(temp.val)
                    child.extend([temp.left,temp.right])
            if result:
                result_return.append(result)
            result = []
            while child:
                temp = child.pop()
                if temp:
                    result.append(temp.val)
                    curr.extend([temp.right,temp.left])
            if result:
                result_return.append(result)
            result = []
        return result_return