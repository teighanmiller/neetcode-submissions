class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate, max_rate = 1, max(piles)
        ans = None

        while min_rate <= max_rate:
            mid = (min_rate + max_rate) // 2

            hours = 0
            for num in piles:
                hours += math.ceil(num/mid)
            
            if hours > h:
                min_rate = mid + 1
            else:
                max_rate = mid - 1
                ans = mid
        return ans


