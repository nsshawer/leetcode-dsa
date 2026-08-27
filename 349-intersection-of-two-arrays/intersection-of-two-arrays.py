class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for n1 in set(nums1):
            if n1 in set(nums2) and n1 not in result:
                result.append(n1)
        
        return result