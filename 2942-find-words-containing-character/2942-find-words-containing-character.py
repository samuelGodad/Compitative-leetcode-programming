class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        index=[]
        for i in range(len(words)):
            if x in words[i]:
                index.append(i)
        return index
            
            
                
        