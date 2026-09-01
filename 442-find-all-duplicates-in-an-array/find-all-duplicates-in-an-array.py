class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for n in nums:
            idx = abs(n) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
            else:
                result.append(idx+1)

        return result
