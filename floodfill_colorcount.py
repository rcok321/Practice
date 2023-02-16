class Solution(object):
    def fill(self, image, sr, sc, R, C, oldColor, newColor):
        if sr == R or sr < 0 or sc < 0 or sc == C:
            return
        if image[sr][sc] == newColor:
            return
        if image[sr][sc] is not oldColor:
            return

        image[sr][sc] = newColor;
        
        
        self.fill(image, sr + 1, sc, R, C, oldColor, newColor)
        self.fill(image, sr - 1, sc, R, C, oldColor, newColor)
        self.fill(image, sr, sc + 1, R, C, oldColor, newColor)
        self.fill(image, sr, sc - 1, R, C, oldColor, newColor)
            
        return
    
    def floodFill(self, image, sr, sc, newColor):
        # print(len(image))
        oldColor = image[sr][sc]
        if (oldColor == newColor):
            return image
        self.fill(image, sr, sc, len(image), len(image[0]), oldColor, newColor)
        # print(hasVisited)
        return image
    
if __name__ == "__main__":
    p = [[1,1,1,2,1],[1,2,1,2,1],[1,1,1,2,3]]
    S = Solution()
    color_set = []
    
    for i in range(len(p)):
        for j in range(len(p[0])):
            p = S.floodFill(p,i,j,0)
            color_set.append(str(p)) 
    print(len(set(color_set)))
            