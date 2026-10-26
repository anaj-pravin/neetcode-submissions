class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            # print(f"left = {l}, right = {r}")
            mid = (l + r) // 2
            # print(f"mid = {mid}")
            eaten = 0

            for p in piles:
                eaten += math.ceil(p / mid)
            # print(f"eaten = {eaten}")
            if eaten <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
            # print(f"res= {res}")
        return res