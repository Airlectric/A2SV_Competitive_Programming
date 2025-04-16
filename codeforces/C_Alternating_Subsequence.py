t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    def alternating(arr,n):
        i = 0
        j = 1
        result = 0

        while j+1 < n:
            if arr[i] > 0 and arr[j] > 0 and arr[i] <= arr[j]:
                i = j
                j += 1
            if arr[i] < 0 and arr[j] > 0 and arr[j+1] > 0 and arr[j] <= arr[j+1]:
                i = j
                j += 1
            elif arr[i] < 0 and arr[j] > 0 and arr[j+1] < 0:
                result += arr[j]
                print('1:',arr[j])
                i = j
                j += 1
            elif arr[i] > 0 and arr[j] < 0 and arr[j+1] < 0 and arr[j] <= arr[j+1]:
                i = j
                j += 1
            elif arr[i] > 0 and arr[j] < 0 and arr[j+1] > 0:
                result += arr[j]
                print('2:',arr[j])
                i = j
                j += 1
            elif arr[i] > 0 and arr[j] < 0 and arr[j+1] > 0:
                result += arr[j]
                print('3:',arr[j])
                i = j
                j += 1
            else:
                i = j
                j += 1
        return result
    
    print(alternating(arr,n))
