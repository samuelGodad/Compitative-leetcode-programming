class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not  grid[0]:
            return 0
        visited =set()
        island =0
        rows=len(grid)
        cols=len(grid[0])
        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c] =='0' or (r,c) in visited ):
                return 
            visited.add((r,c))
            direction =[[0,1],[0,-1],[1,0],[-1,0]]
            for dr,dc in direction:
                dfs(r+dr ,c+dc)
            
        for r in range(rows):
            for c in range (cols):
                if grid[r][c]=='1' and (r,c) not in visited :
                    island+=1
                    dfs(r,c)
        return island
                    
        