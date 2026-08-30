class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        writer = 0

        for i, n in enumerate(nums):
            if n != 0:
                nums[writer], nums[i] = nums[i], nums[writer]
                writer += 1        