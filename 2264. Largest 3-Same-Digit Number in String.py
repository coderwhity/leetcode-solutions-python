class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = -1
        for i in range(0,len(num)-2):
            if(num[i:i+3] == num[i]*3 and int(num[i])>=int(l)):
                l = num[i]
        return l*3 if l!=-1 else ""
