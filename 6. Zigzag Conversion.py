class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ri = 0 #row index
        rows = [[] for row in range(numRows)]
        rm = False # reverse iteration mode
        for c in s:
            if not rm:
                if(ri<numRows):
                    rows[ri].append(c)
                    ri+=1
                else:
                    rm = True
                    ri-=2
                    rows[ri].append(c)
            else:
                ri-=1
                if(ri==-1):
                    ri=2
                    rows[1].append(c)
                    rm = False
                else:
                    rows[ri].append(c)

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)
