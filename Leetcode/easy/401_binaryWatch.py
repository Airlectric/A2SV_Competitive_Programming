class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        def setbitCount(num):
            counter = 0
            while num:
                counter += num & 1
                num >>= 1
            return counter

        for hour in range(12):
            for minute in range(60):
                if setbitCount(hour) + setbitCount(minute) == turnedOn:
                    res.append(f'{hour}:{minute:02d}')
        return res

       



        
