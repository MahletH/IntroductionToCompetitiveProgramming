class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        matrix=[]
        for i in range(R):
            cell=[]
            cell.append(i)
            for j in range(C):
                cell.append(j)
                matrix.append(cell)
                cell=cell[:len(cell)-1]
        
        dist=[]
        for i in range(R):
            for j in range(C):
                dist.append(abs(i-r0)+abs(j-c0))
        maxNum= max(dist)
        matrix2=[]
        for k in range(maxNum+1):
            for j in range(len(dist)):
                if(dist[j]==k):
                    matrix2.append(matrix[j])
        
        return matrix2
