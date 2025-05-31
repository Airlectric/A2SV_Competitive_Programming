def bisectRight(arr,target):
	n = len(arr)
	left = 0
	right = n-1

	while left < right:
		mid = left + (right-left) // 2
		if arr[mid] <= target:
			left = mid + 1
		else:
			right = mid

	return arr[left]



if __name__ == "__main__":
	arr = [x for x in range(9)]
	print(arr)
	print(bisectRight(arr,6))

