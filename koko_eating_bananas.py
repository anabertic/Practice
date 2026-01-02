class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        potential_k = max(piles)
        while l<=r:
            mid = (l + r)//2
            calculated_hours = self.calculate_hours(mid,h,piles) 
            if calculated_hours <= h:
                potential_k = min(potential_k, mid)
                r = mid - 1
            else:
                l = mid + 1
        return potential_k

    def calculate_hours(self, k, h, piles):
        hours = 0
        for i in range(0, len(piles)):
            hours += math.ceil(piles[i]/k)
        return hours

        
