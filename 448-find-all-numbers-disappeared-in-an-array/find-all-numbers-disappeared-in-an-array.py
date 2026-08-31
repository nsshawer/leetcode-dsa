class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # --- O(n) SOLUTION ---

        # length = len(nums)
        # hash_table = [0] * (length + 1)
        # result = []

        # for n in nums:
        #     if n < len(hash_table):
        #         hash_table[n] += 1

        # for i, h in enumerate(hash_table):
        #     if h == 0 and i != 0:
        #         result.append(i)
        
        # return result

        # --- O(1) SOLUTION ---
        result = []

        for n in nums:
            indx = abs(n)-1
            nums[indx] = -abs(nums[indx])
        
        for i, n in enumerate(nums):
            if n > 0:
                result.append(i+1)

        return result