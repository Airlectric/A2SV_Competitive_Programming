class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        compared = x ^ y
        count = 0

        while compared:
            if compared % 2 == 1:
                count += 1
            compared //= 2
        
        return count
