class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        reader = 0

        for i, n in enumerate(nums):
            if nums[reader] != n:
                nums[reader+1], nums[i] = nums[i], nums[reader+1]
                reader += 1
            
        return reader+1