class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = 0
        digit_sum = 0

        for num in nums:
            element_sum += num
            digits = [int(d) for d in str(num)]
            for d in digits:
                digit_sum += d

        return abs(element_sum - digit_sum)