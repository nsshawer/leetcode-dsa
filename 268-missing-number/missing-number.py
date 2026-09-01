class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_table = [0] * (len(nums) + 1)

        for n in nums:
            hash_table[n] += 1

        print(hash_table)
        
        for i, h in enumerate(hash_table):
            if h == 0:
                return i