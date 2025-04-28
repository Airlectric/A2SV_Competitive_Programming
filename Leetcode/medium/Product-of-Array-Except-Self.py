class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefixProduct = [1] * n

        for i in range(1,n):
            prefixProduct[i] = prefixProduct[i-1] * nums[i-1]

        suffixProduct = [1] * n

        for i in range(n-2, -1, -1):
            suffixProduct[i] = suffixProduct[i+1] * nums[i+1]

        result = []
        for i in range(n):
            result.append(prefixProduct[i] * suffixProduct[i])

        return result 


        