class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        ans = []

        for i in nums:
            seen[i] = seen.get(i, 0) + 1

        sorted_val = sorted(seen.items(), 
        key = lambda x: x[1], reverse = True)

        for i in sorted_val[0:k]:
            ans.append(i[0])

        return ans