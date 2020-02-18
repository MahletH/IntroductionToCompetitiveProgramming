import heapq
class Words:
    def __init__(self,word: str, freq:int):
        self.word=word
        self.freq=freq
    def __eq__(self, other):
            return (self.__class__ == other.__class__ and self.freq == other.freq and self.word == other.word)
    def __lt__(self, other):
            return (self.__class__ == other.__class__ and self.freq > other.freq or self.freq == other.freq and self.word < other.word)
    def __gt__(self, other):
            return (self.__class__ == other.__class__ and self.freq < other.freq or self.freq == other.freq and self.word > other.word)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count={}
        lst=[]
        for word in words:
            if word in count:
                count[word]+=1
            else:
                count[word]=1
        for word in count:
            new_word=Words(word,count[word])
            lst.append(new_word)
        heapq.heapify(lst)
        return [heapq.heappop(lst).word for _ in range(k)]
