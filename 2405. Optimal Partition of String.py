# Amazon Spring '23 High Frequency'
Amazon Spring '23 High Frequency
class Solution:
    def partitionString(self, s: str) -> int:
        w_l = 0
        curr_lw = ""
        for c in s:
            if c in curr_lw:
                w_l+=1
                curr_lw = c
            else:
                curr_lw+=c
        if len(s)!=0:w_l+=1
        return w_l
