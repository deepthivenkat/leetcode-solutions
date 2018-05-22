class Solution(object):
    def count_water(self,grid,idx_r,idx_c):
        cur_peri =0
        adj = [(idx_r-1,idx_c),(idx_r+1,idx_c),(idx_r,idx_c-1),(idx_r,idx_c+1)]
        for x,y in adj:
            if x< 0 or y<0 or x==len(grid) or y==len(grid[0]) or not grid[x][y]:
                cur_peri += 1
        return cur_peri
                
    def islandPerimeter(self, grid):
        if not grid:
            return 0
        peri = 0
        len_c = len(grid)
        len_r = len(grid[0])
        for idx_r,row in enumerate(grid):
            for idx_c,col in enumerate(row):
                if grid[idx_r][idx_c]:
                    peri += self.count_water(grid,idx_r,idx_c)
        return peri