class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        titleNum = 0

        for i in range(len(columnTitle)):

            letValue = (ord(columnTitle[i]) - ord('A')) + 1

            titleNum = (titleNum * 26) + letValue

        return titleNum
    
      
        
