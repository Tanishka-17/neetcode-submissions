class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        left=1
        right=max(piles)
        answer=max(piles)
        hours=0
        while left<=right:
            hours=0
            mid=(left+right)//2
            k=mid
            for i in piles:
                hours += math.ceil(i/k)
            
            if hours <= h:
                answer=min(answer,k)
                right=mid-1
            else:
                left=mid+1
        return answer

            