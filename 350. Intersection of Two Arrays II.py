class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Converting list to sets to remove duplicate elements and then getting intersecting elements in both the list(set) and thewn converting that intersecting set to list.
        s1 = list(set(nums1) & set(nums2))
        # Final array which will be returned
        f = []
        # Iterating through all the elements in s1 (Intersecting elements)
        for n in s1:
            # Extending or inserting n element in list for count which is the minimum number of count in both lists
            f += [n]*min(nums1.count(n) , nums2.count(n))
        
        # Returning list
        return f
