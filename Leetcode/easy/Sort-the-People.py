class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        map_names = {}

        for i in range(len(names)):
            map_names[heights[i]] = names[i]

        n = len(heights)

        # Count sort
        count_arr = [0] * (max(heights)+1)

        for height in heights:
            count_arr[height] += 1

        target = 0
        for i in range(len(count_arr)-1,-1,-1):
            for _ in range(count_arr[i]):
                heights[target] = i
                target += 1
            
        return [map_names[height] for height in heights]

        
        


        