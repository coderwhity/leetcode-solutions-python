class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)        
        rv =[]
        for x in s:
            if x in 'aeiouAEIOU':
                rv.append(x)
        for i in range(0,len(s)):
            if s[i] in 'aeiouAEIOU':
                s[i] = rv.pop()
        return ''.join(s)
