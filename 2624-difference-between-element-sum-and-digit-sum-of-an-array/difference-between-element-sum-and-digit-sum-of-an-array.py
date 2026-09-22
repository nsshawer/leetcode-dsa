class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0

        for n in nums:
            while n > 0:
                digit_sum += (n % 10)
                n = n // 10

        return abs(element_sum - digit_sum)