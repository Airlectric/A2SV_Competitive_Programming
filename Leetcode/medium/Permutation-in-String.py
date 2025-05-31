from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        detectS1 = defaultdict(int)
        detectS2 = defaultdict(int)
        k = len(s1)

        for i in range(k):
            detectS1[s1[i]] += 1
        
        for i in range(k):
            if i < len(s2):
                detectS2[s2[i]] += 1

        start = 0

        for end in range(k,len(s2)):
            if detectS1 == detectS2:
                return True

            if detectS2[s2[start]] > 1:
                detectS2[s2[start]] -= 1
            else:
                del detectS2[s2[start]]

            detectS2[s2[end]] += 1
            start += 1

        if detectS1 == detectS2:
                return True

        return False

            

        
        