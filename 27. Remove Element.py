class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(0,len(nums)):
            for j in range(0,len(nums)-1):
                if nums[j] == val:
                    nums[j+1],nums[j] = nums[j],nums[j+1]
        return len(nums)-nums.count(val)
