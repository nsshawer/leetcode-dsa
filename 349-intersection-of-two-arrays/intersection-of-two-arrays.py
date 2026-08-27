class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for n1 in nums1:
            if n1 not in result:
                if n1 in nums2:
                    result.append(n1)
        
        return result