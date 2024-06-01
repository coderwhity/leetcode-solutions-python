class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # List integer which will be returned
        f = []

        # Store first and last index of c
        # initially both will be same
        first = s.find(c)
        last = first

        # Itterating through string
        for i in range(0,len(s)):
            # Calculating distance from both first and last index and then storing shortest ditance
            f.append(min(abs(i-first),abs(i-last)))
            # Check if current index is at our c index which is last
            if(i == last):
                # If True then we will transfer pointer 
                #  First <- Last
                #  Last <- Find next index of c 
                first,last = last,s.find(c,last+1)
                
        # Returning List
        return f
