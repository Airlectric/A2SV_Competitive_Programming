from collections import Counter
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leaders = []
        self.count = Counter()

        leader = -1
        max_count = 0

        for person in persons:
            self.count[person] += 1

            if self.count[person] >= max_count:
                if person != leader:
                    leader = person
                max_count = self.count[person]
            self.leaders.append(leader)
        

    def q(self, t: int) -> int:
        n = len(self.times)
        left = 0
        right = n-1

        while left <= right:
            mid = left + (right - left) // 2

            if self.times[mid] <= t:
                left = mid + 1
            else:
                right = mid - 1
        
        return self.leaders[right]

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)