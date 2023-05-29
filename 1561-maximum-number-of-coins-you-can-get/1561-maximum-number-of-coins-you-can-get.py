class Solution:
   def maxCoins(self,piles):
        piles.sort(reverse=True)
        total_coins = 0
        index = 0
        remaining = len(piles)

        while remaining > 2:
            total_coins += piles[index + 1]
            index += 2
            remaining -= 3

        return total_coins

