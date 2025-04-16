class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        current = len(arr)

        result = []

        while current > 1:
            max_idx = arr.index(max(arr[:current]))

            arr = arr[max_idx::-1] + arr[max_idx+1:]

            arr = arr[current-1::-1] + arr[current:]

            result.append(max_idx+1)
            result.append(current)

            current -= 1
        print(arr)
        return result  