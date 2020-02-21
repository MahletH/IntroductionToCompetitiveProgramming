import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p="!?',;. "
        max_=-1
        max_word=''
        punc=set()
        for i in p:
            punc.add(i)
        banned_set=set()
        for word in banned:
            banned_set.add(word)
        occurrance={}
        words=[]
        res=''
        for i in paragraph:
            print(i)
            if i not in punc:
                res=res+i
            else:
                if res != '':
                    words.append(res)
                    res=''
        if res != '':
            words.append(res)
        for word in words:
            word=word.lower()
            if word in occurrance:
                occurrance[word]+=1
            else:
                occurrance[word]=1
        for word in occurrance:
            if word in banned:
                continue
            else:
                if max_ < occurrance[word]:
                    max_=occurrance[word]
                    max_word=word
        return max_word
