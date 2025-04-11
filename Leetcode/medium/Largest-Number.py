class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        new_arr = list(map(str,nums))

        result = \\

        for i in range(len(new_arr)-1):
            for j in range(len(new_arr)-i-1):
                if new_arr[j+1] + new_arr[j] > new_arr[j] + new_arr[j+1]:
                    new_arr[j+1], new_arr[j] = new_arr[j], new_arr[j+1]

        for num in new_arr:
            result += num

        return \0\ if result[0] == '0' else result
        