class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        largest = 0
        if len(s) == 1 : return 1
        else:
            for i in range(0,len(s)):
                cur =""
                for j in range(i,len(s)): 
                    if s[j] in cur:break 
                    else:cur+=s[j]
                largest = max(largest,len(cur))
            return largest
