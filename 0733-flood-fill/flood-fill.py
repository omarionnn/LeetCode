class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        old = image[sr][sc]
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (r, c) in visit:
                return 
            if (min(r, c) < 0 or r == rows or c == cols or image[r][c] != old):
                return 

            visit.add((r, c))
            image[r][c] = color
            for dr, dc in directions:
                row, col = dr + r, dc + c
                dfs(row, col)

        dfs(sr, sc)
        return image
        