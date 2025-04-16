class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        counter = 0

        for i in range(len(timeSeries)):
            if i+1 < len(timeSeries) and timeSeries[i]+duration < timeSeries[i+1]:
                counter += duration
            else:
                if i+1 < len(timeSeries):
                    counter += timeSeries[i+1] - timeSeries[i]
        counter += duration

        return counter

        
