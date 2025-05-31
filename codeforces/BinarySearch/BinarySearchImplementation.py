def binarySearch(arr,target):
	n = len(arr)
	left = 0
	right = n-1

	while left <= right:
		mid = left + (right-left) // 2
		print('mid',mid)
		if arr[mid] == target:
			return arr[mid]
		elif arr[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return -1



if __name__ == "__main__":
	arr = [x for x in range(9)]
	print(arr)
	print(binarySearch(arr,6))

