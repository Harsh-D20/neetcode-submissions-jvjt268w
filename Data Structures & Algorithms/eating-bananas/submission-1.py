class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            m = left + ((right - left) // 2)
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
            if hours <= h:
                ans = m
                right = m - 1
            else:
                left = m + 1
        return ans