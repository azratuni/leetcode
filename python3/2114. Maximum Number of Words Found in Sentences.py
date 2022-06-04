class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        i = 0
        for sentence in sentences:
            x = len(sentence.split())
            if x>i:
                i=x
        return i