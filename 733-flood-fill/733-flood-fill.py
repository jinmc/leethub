class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        seen = set()
        def dfs(i, j, image, origColor, newColor):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or (i, j) in seen or image[i][j] != origColor:
                return
            seen.add((i, j))
            image[i][j] = newColor
            u = dfs(i, j+1, image, origColor, newColor)
            d = dfs(i, j-1, image, origColor, newColor)
            r = dfs(i+1, j, image, origColor, newColor)
            l = dfs(i-1, j, image, origColor, newColor)
        
            
        dfs(sr, sc, image, image[sr][sc], newColor)
        return image