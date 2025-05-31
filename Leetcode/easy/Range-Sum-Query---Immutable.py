class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        n = len(self.nums)
        prefixSum = [0] * (n+1)

        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + self.nums[i]

        sumRange = prefixSum[right+1] - prefixSum[left]

        return sumRange

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)