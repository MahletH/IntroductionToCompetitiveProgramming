class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        grid=[[float('inf') for _ in range(n)] for _ in range(n)]
        for edge in edges:
            grid[edge[0]][edge[1]]=grid[edge[1]][edge[0]]=edge[2]
        for k in range(n):
            for i in range(n):
                for j in range(i+1,n):
                    grid[i][j]=grid[j][i]=min(grid[i][k]+grid[j][k],grid[i][j])
        city_neighbour=[]
        for i in range(n):
            city_count=0
            for dist in grid[i]:
                if dist<=distanceThreshold:
                    city_count+=1
            city_neighbour.append(city_count)
        min_=float('inf')
        min_index=0
        for i,num_cities in enumerate(city_neighbour):
            if num_cities<=min_:
                min_=num_cities
                min_index=i
        return min_index
def solution(n, edges, distanceThreshold):
    s = Solution()
    return s.findTheCity(n, edges, distanceThreshold)


def main():
    n = 5
    edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
    distanceThreshold = 5
    print(solution(n, edges, distanceThreshold))


if __name__ == '__main__':
    main()
            
