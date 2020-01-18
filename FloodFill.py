class Solution:
    def fill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        neighbours=[[0,-1],[-1,0],[0,1],[1,0]]
        prevColor=image[sr][sc]
        image[sr][sc]=newColor
        cell=[sr,sc]
        for i in neighbours:
            r=cell[0]+i[0]
            c=cell[1]+i[1]
            if(r>=0 and r<len(image) and c>=0 and c<len(image[0])):
                if(image[r][c]==prevColor):
                    
                    self.fill(image,r,c,newColor)
                    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if(image[sr][sc]==newColor):
            return image
        self.fill(image,sr,sc,newColor)
        return image
                
                
        
