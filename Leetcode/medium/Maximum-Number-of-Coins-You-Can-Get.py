class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort(reverse=True)

        num_of_picks = len(piles)/3

        mycoins = 0
        picks = 0
        
        for i in range(1,len(piles),2):
            if picks < num_of_picks:
                mycoins += piles[i]
                picks += 1

        return mycoins


        