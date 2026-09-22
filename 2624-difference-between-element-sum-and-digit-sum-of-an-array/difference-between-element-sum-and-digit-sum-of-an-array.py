class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0

        for n in nums:
            digits = [int(d) for d in str(n)]
            for d in digits:
                digit_sum += d

        return abs(element_sum - digit_sum)
        