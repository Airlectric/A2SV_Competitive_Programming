from collections import defaultdict
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruitss: List[int]
        :rtype: int
        """
        maximum = 0
        start = 0
        detect = defaultdict(bool)

        for end in range(len(fruits)):
            if fruits[end] not in detect and len(detect)<2:
                detect[fruits[end]] = True
                if (end-start+1) > maximum:
                    maximum = (end-start+1)
            elif fruits[end] in detect:
                if (end-start+1) > maximum:
                    maximum = (end-start+1)
            else:
                detect = defaultdict(bool)
                detect[fruits[end-1]] = True
                detect[fruits[end]] = True
                start = end -1

                while fruits[start-1] == fruits[start]:
                    start-=1
                
                if (end-start+1)>maximum:
                    maximum = (end-start+1)
        return maximum

            


                
