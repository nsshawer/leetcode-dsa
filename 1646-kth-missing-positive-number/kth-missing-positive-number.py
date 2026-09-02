class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        missing = []

        for a in range(1, k + len(arr) + 1):
            if a not in arr_set:
                missing.append(a)
        
        return missing[k-1]