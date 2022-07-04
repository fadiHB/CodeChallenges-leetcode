class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image == None or image[sr][sc] == color:
            return image
        
        self.fill(image, sr, sc, image[sr][sc], color)
        
        return image
    
    
    def fill(self, image, r, c, initial, color):
        
        # Base Cases
        ## check the out of bounds
        rCond = (r < 0) or (r >= len(image))
        cCond = (c < 0) or (c >= len(image[0]))
        
        if rCond or cCond:
            return
        
        ## check if we go back to the initial point
        if (image[r][c] != initial):
            return
        
        image[r][c] = color
        
        # Recursion Case
        self.fill(image, r+1, c, initial, color) #down, next row
        self.fill(image, r-1, c, initial, color) #up, prev row
        self.fill(image, r, c+1, initial, color) #right, next column
        self.fill(image, r, c-1, initial, color) #left, prev column
        
        
        