class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        start_pos = len(nums1)-n
        for x in nums2:
            nums1[start_pos] = x
            start_pos+=1
        nums1.sort()
