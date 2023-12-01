class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(sl1,sl2):
            s = sl1
            while s > 0:
                if sl1%s==0 and sl2%s == 0:
                    return s
                else:
                    s-=1
            return s
        if str1+str2 == str2+str1:
            l1 = len(str1)
            l2 = len(str2)
            if l1 > l2:
                l1,l2=l2,l1
            return str1[0:gcd(l1,l2)]
        else:   
            return ""
