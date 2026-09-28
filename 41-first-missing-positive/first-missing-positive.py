class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        num_set = set(nums)
        for n in range(1, len(nums)+2):
            if n not in num_set:
                return n
