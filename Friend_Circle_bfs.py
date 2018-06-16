from collections import deque
class Solution(object):
    def findCircleNum(self, M):
        visited,n_cc,len_M = set(),0,len(M)
        if not len_M:
            return 0
        len_i = len(M[0])
        for i in range(len_M):
            if i in visited:
                continue
            else:
                queue = deque([i])
                while queue:
                    curr = queue.popleft()
                    visited.add(curr)
                    neigh = M[curr]
                    for idx,val in enumerate(neigh):
                        if val and idx not in visited:
                            queue.extend([idx])
                n_cc+=1
        return n_cc
        
        
            
        
        
        """
        :type M: List[List[int]]
        :rtype: int
        """
        