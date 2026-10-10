class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        r = 0
        count = {}
        n = len(s) 
        diff = 0
        window = 0

        while r < n:
            count[s[r]] = count.get(s[r], 0) + 1
            diff = (r - l + 1) - max(count.values())

            if diff > k:
                count[s[l]] = count.get(s[l]) - 1
                l = l + 1

            res = max(res, r - l + 1)
            r = r + 1
            # print(count)
            # print(res)
            # print(diff)
            # print(r - l)

        return res