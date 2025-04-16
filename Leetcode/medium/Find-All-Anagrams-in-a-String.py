from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)

        k = len(p)

        result = s[:k]
        current = Counter(result)
        annagram = []

        for r in range(k, len(s)):
            l = r - k

            if current == target:
                annagram.append(l)

            current[s[l]] -= 1
            current[s[r]] += 1

        if current == target: annagram.append(len(s)-k)

        return annagram


        