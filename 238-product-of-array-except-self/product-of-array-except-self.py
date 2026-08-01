class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1
        suffix = 1

        for i, num in enumerate(nums):
            answer[i] = prefix
            prefix *= num
        
        for i, a in enumerate(nums[::-1]):
            real_indx = len(nums) - 1 - i
            answer[real_indx] *= suffix
            suffix *= a         

        return answer