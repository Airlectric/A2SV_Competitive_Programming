class Solution:
    def countSegments(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        count = 0
        
        s = s.split(' ')

        for word in s:
            if word != '':
                count+=1
        
        return count
        
