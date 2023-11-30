class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = "0"*(len(a)-len(b))+b
        elif len(b) > len(a):
            a = "0"*(len(b)-len(a))+a
        ans = ""
        c = 0

        for i in range(0,len(a)):
            if  a[len(a)-1-i] == "1" and b[len(b)-1-i] == "1":
                if c == 1:
                    ans += "1"
                else:    
                    ans += "0"
                    c = 1
            elif a[len(a)-1-i] == "0" and b[len(b)-1-i] == "0":
                if c == 1:
                    ans += "1"
                    c = 0
                else:    
                    ans += "0"
            elif (a[len(a)-1-i] == "1" and b[len(b)-1-i] == "0") or a[len(a)-1-i] == "0" and b[len(b)-1-i] == "1":
                if c == 1:
                    ans += "0"
                    c = 1
                else:    
                    ans += "1"
        
        if c == 1:
            ans += "1"
        return ans[::-1]
