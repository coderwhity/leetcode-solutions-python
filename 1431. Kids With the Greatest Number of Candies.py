class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = [True if k+extraCandies >= max_candies else False for k in candies]
        return result
