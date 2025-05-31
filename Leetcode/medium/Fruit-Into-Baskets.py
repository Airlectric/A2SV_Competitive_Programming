from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        max_ = float('-inf')
        n = len(fruits)
        count = 0
        start = 0

        for end in range(n):
            if fruits[end] not in basket and len(basket) < 2:
                basket[fruits[end]] += 1
                count += 1
                max_ = max(max_, count)
            elif fruits[end] in basket and len(basket) <= 2:
                basket[fruits[end]] += 1
                count += 1
                start = end
                max_ = max(max_, count)
            else:
                del basket
                basket = defaultdict(int)
                count = 0

                start = end-1
                while fruits[end-1] == fruits[start]:
                    basket[fruits[start]] += 1
                    start -= 1
                    count += 1

                basket[fruits[end]] += 1
                count += 1
        
        return max_
            
            







        