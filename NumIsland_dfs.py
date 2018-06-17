class Solution(object):
    def get_adj(self,i,j):
        return [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    def dfs(self,i,j,m,n): 
        if 0<=i<m and 0<=j<n and self.grid[i][j]=='1':
            self.grid[i][j]='0'
            adj_pts = self.get_adj(i,j)
            for pt in adj_pts:
                self.dfs(pt[0],pt[1],m,n)
            return 1
        return 0
            
    def numIslands(self, grid):
        num_island = 0
        if not grid:
            return num_island
        self.grid = grid
        len_rows = len(grid)
        len_cols = len(grid[0])
        for i,r in enumerate(self.grid):
            for j,c in enumerate(r):
                num_island+=self.dfs(i,j,len_rows,len_cols)           
        return num_island