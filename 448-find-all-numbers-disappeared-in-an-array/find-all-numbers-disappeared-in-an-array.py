class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        hash_table = [0] * (length + 1)
        result = []

        for n in nums:
            if n < len(hash_table):
                hash_table[n] += 1

        for i, h in enumerate(hash_table):
            if h == 0 and i != 0:
                result.append(i)
        
        return result