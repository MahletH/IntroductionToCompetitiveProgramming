class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        ctr=0
        prev=0
        prevMax=-1
        for clip in clips:
            if clip[0]<=prev:
                if prevMax<clip[1]:
                    prevMax=clip[1]
            else:
                if clip[0]>prevMax:
                    return -1
                ctr+=1
                prev=prevMax
                if prevMax<clip[1]:
                    prevMax=clip[1]
            if prevMax>=T and T!=0:
                ctr+=1
                break
        if prevMax<T:
            return -1
        return ctr
                
