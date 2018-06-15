
class Solution(object):
    def findCircleNum(self, M):
        visited,n_cc,len_M = set(),0,len(M)
        def dfs(matrix,i,len_matrix):
            curr_person = matrix[i]
            for idx,j in enumerate(curr_person):
                if j and idx not in visited:
                    visited.add(idx)
                    dfs(matrix,idx,len_matrix)
            return

        len_i = len(M[0])
        for i in range(len_M):
            if i not in visited:
                dfs(M,i,len_i)
                n_cc += 1
        return n_cc