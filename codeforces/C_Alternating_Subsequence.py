t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    def alternating(arr,n):
        current = arr[0]
        result = 0

        for i in range(1,n):
            if (current > 0 and arr[i] > 0) or (current < 0 and arr[i] < 0):
                current = max(current, arr[i])
            else:
                result += current
                current = arr[i]
        
        result += current

        return result
    
    print(alternating(arr,n))

