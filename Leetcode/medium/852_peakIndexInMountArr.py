class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        pt1 = 0
        pt2 = len(arr)-1

        while pt1 < pt2:
            mid = (pt1 + pt2) // 2

            if arr[mid] <  arr[mid+1]:
                pt1 = mid+1
            elif arr[mid] > arr[mid+1]:
                pt2 = mid
                
        return pt1
            

    
        
