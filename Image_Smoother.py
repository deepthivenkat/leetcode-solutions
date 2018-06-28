class Solution(object):
    def get_neigh(self,i,j,num_rows,num_cols):
        neigh_list = [(i+1,j),(i,j+1),(i-1,j),(i,j-1),(i-1,j-1),(i+1,j+1),(i+1,j-1),(i-1,j+1)]
        neigh_list = filter(lambda x: not x[0]<0 and not x[1]<0 and not x[0]>=num_rows and not x[1]>=num_cols,neigh_list)
        return neigh_list
    def imageSmoother(self, M):
        new_M = [[0 for i in M[0]] for j in M]
        num_rows = len(M)
        num_cols = len(M[0])
        for idx_r,i in enumerate(M):
            for idx_c,j in enumerate(i):
                new_M[idx_r][idx_c] += M[idx_r][idx_c]
                neighs = self.get_neigh(idx_r,idx_c,num_rows,num_cols)
                new_M[idx_r][idx_c] += sum([M[p][q] for p,q in neighs])
                new_M[idx_r][idx_c] = new_M[idx_r][idx_c]//(len(neighs)+1)
        return new_M