class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(numbers):
            remainder = target - num

            if remainder in seen:
                if i+1 > seen[remainder]+1:
                    return [seen[remainder]+1, i+1]
                return [[i+1, seen[remainder]+1]]

            seen[num] = i