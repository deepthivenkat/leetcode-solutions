class Solution(object):
    def nextGreaterElement(self, n):
        n,len_n,found = map(int,str(n)), len(str(n)),False
        for idx in range(len_n-1,0,-1):
            if n[idx-1] < n[idx]:
                found = True
                break
        if not found:
            return -1
        to_swap = idx-1
        min_num,min_idx = None,None
        for inx,x in enumerate(n[idx:]):
            if (not min_num or (min_num and x<min_num)) and x>n[to_swap]:
                min_idx = idx+inx
                min_num = x
        n[to_swap], n[min_idx] = n[min_idx], n[to_swap]
        n[to_swap+1:]=sorted(n[to_swap+1:])
        ret_num = int(''.join(map(str,(n))))
        return ret_num if ret_num<= 2147483647 else -1