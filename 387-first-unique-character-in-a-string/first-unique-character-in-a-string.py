class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}

        for char in s:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
                    
        for key, value in seen.items():
            if value == 1:
                return s.index(key)

        return -1