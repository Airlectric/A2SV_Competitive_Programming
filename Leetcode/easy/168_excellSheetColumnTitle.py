class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = []
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            letter = chr(remainder + ord('A'))
            title.append(letter)
            columnNumber //= 26
        return ''.join(reversed(title))

        
