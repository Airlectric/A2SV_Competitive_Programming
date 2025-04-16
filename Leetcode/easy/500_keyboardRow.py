class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        for i in range(len(words)):
            j = 0
            if words[i][0].lower() in rows[0]:
                while j < len(words[i]) and words[i][j].lower() in rows[0]:
                    j += 1
                if j == len(words[i]):
                    res.append(words[i])
            if words[i][0].lower() in rows[1]:
                while j < len(words[i]) and words[i][j].lower() in rows[1]:
                    j += 1
                if j == len(words[i]):
                    res.append(words[i])
            if words[i][0].lower() in rows[2]:
                while j < len(words[i]) and words[i][j].lower() in rows[2]:
                    j += 1
                if j == len(words[i]):
                    res.append(words[i])

        return res
            

        
