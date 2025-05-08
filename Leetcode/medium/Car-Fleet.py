class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        values = []
        n = len(position)
        unique_fleet = []

        for i in range(n):
            time = (target - position[i])/ speed[i]
            values.append((position[i],time))
        
        values.sort(key=lambda x:x[0])

        for i in range(n-1,-1,-1):

            if not unique_fleet or values[i][1] > unique_fleet[-1]:
                unique_fleet.append(values[i][1])
        
        return len(unique_fleet)

        