class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ind = 1
        for c in word2:
            word1 = word1[:ind]+c+word1[ind:]
            ind+=2
        return word1
