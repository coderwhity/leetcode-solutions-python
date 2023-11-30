class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        i,prf = len(strs[0]),""
        while i >= 0:
            # l is list that will contain matched words
            prf,l = strs[0][0:i],[]
            for x in strs:
                if x[0:i]==prf:
                    l.append(x)
            if len(l) == len(strs):
                return prf
            i-=1        
        return ""
