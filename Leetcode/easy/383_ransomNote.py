from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        detectR = Counter(ransomNote)
        detectM = Counter(magazine)

        for i in range(len(ransomNote)):
            if detectR[ransomNote[i]] > detectM[ransomNote[i]]:
                return False
        
        return True

        
