class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        reference = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        def dfs(image, color, r, c, visit, reference):
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in visit or image[r][c] != reference:
                return
            
            image[r][c] = color
            visit.add((r,c))
            dfs(image, color, r+1, c, visit, reference)
            dfs(image, color, r-1, c, visit, reference)
            dfs(image, color, r, c+1, visit, reference)
            dfs(image, color, r, c-1, visit, reference)
        dfs(image, color, sr, sc, set(), reference)
        return image