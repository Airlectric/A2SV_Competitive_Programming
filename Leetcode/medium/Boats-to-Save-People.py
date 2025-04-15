class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        N = len(people)

        i = 0
        j = N-1
        boats = 0

        while i <= j:
            if people[i] + people[j] > limit:
                boats += 1
                j -= 1
            elif people[i] + people[j] == limit:
                boats += 1
                i += 1
                j -= 1
            elif people[i] + people[j] < limit:
                boats += 1
                i += 1
                j -= 1
            elif i == j and people[i] <= limit:
                boat += 1

        return boats

        
            
        