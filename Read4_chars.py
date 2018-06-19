from collections import deque
class Solution(object):
    def __init__(self):
        self.queue,self.queue_len = deque([]),0
    def read(self, buf, n):
        if n==0:
            return 0
        total_idx,read_idx = 0,0
        while self.queue_len<n:
            curr_buffer = [""]*4
            k = read4(curr_buffer)
            if k==0:
                break
            curr_buffer = filter(lambda x:x!="",curr_buffer)
            self.queue.extend(curr_buffer)
            self.queue_len += k
        while n-read_idx and self.queue:
            #print self.queue, read_idx
            buf[read_idx] = self.queue.popleft()
            self.queue_len-=1
            read_idx+=1
        return read_idx