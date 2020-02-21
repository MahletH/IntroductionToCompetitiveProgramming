class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans=[0]*len(A)
        cur_ptr=len(A)-1
        left_ptr,right_ptr=0,len(A)-1
        while left_ptr<=right_ptr:
            if abs(A[left_ptr])>abs(A[right_ptr]):
                ans[cur_ptr]=(A[left_ptr])**2
                left_ptr+=1
            else:
                ans[cur_ptr]=(A[right_ptr])**2
                right_ptr-=1
            cur_ptr-=1
        return ans
            
