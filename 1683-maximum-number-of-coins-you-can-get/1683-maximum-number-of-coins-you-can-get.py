class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i=len(piles)-2
        j=0
        total=0

        while j<len(piles)//3:
            total+=piles[i]
            i-=2
            j+=1
        return total
       
