class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        n = len(skill)

        i = 0
        j = n-1

        fair_skill = []
        chemistry = 0
        
        while i < j:
            fair_skill.append(skill[i] + skill[j])

            chemistry += skill[i] * skill[j]
            if len(fair_skill) > 1 and fair_skill[0]!=fair_skill[-1]:
                return -1

            i += 1
            j -= 1
        
        return chemistry




        