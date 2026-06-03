class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        hi = max(piles)
        result = hi
        while l <= hi:
            total = 0
            mid = l + (hi-l)//2
            for pile in piles:
                total = total + math.ceil(pile/mid)
            if total > h:
                l = mid + 1
            else:
                res = mid
                hi = mid - 1
        return res




        