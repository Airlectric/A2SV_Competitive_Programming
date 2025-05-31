class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)

        if n < 3:
            return False
        
        pivot = arr.index(max(arr))

        if pivot == 0 or pivot == n-1:
            return False

        for i in range(pivot):
            if arr[i] >= arr[i+1]:
                return False
        
        for i in range(pivot, n-1):
            if arr[i] <= arr[i+1]:
                return False
        
        return True
        