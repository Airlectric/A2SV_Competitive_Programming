class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o','u']
        s = list(s)

        pt1, pt2 = 0, len(s)-1

        while pt1 < pt2:
            if s[pt1].lower() in vowels and s[pt2].lower() in vowels:
                holder = s[pt1]
                s[pt1] = s[pt2]
                s[pt2] = holder
                pt1 += 1
                pt2 -= 1
            elif s[pt1].lower() not in vowels:
                pt1 += 1
            elif s[pt2].lower() not in vowels:
                pt2 -= 1

        return ''.join(s)


            
        
