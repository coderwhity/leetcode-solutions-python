class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 7:
            n = sum(int(x) ** 2 for x in str(n))
            if n == 4:
                return False
        return True
