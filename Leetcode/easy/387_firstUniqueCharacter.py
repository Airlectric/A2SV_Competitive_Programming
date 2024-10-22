class Solution:
    def firstUniqChar(self, s: str) -> int:
        detect = {}

        for letter in s:
            detect[letter] = detect.get(letter,0)+1

        for i in range(len(s)):
            if detect[s[i]] == 1:
                return i
        return -1
        

        
        
