class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            remainder = target - num

            if remainder in nums:
                rem_indx = nums.index(remainder)
                if rem_indx != i:
                    return [i, rem_indx]