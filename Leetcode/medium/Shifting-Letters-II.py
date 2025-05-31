class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefixSum = [0] * (n+1)

        arr = [0] * n

        for shift in shifts:
            if shift[2] == 0:
                arr[shift[0]] -= 1
                if shift[1] < n-1:
                    arr[shift[1]+1] += 1
            else:
                arr[shift[0]] += 1
                if shift[1] < n-1:
                    arr[shift[1]+1] -= 1


        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + arr[i]

        res = ""
        for i in range (n):
            char_num = (ord(s[i]) - ord('a') + prefixSum[i+1]) % 26
            character = chr(char_num + ord('a'))
            res += character

        return res





        