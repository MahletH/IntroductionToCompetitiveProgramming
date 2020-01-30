class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1={}
        dict2={}
        for i in arr:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for i in dict1:
            if dict1[i] in dict2:
                return False
            dict2[dict1[i]]=i
            
        return True
