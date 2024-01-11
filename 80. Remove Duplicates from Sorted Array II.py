class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for x in nums:
            c = nums.count(x)
            for y in range(0,c-2):
                nums.pop(nums.index(x))
                
