class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lst=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        visited=set()
        for word in words:
            mor=''
            for c in word:
                mor=mor+(lst[ord(c)-ord('a')])
            if mor not in visited:
                visited.add(mor)
        return len(visited)
