class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        ans = []

        for i, val in enumerate(strs):
            temp = "".join(sorted(val))
            if temp not in seen:
                seen[temp] = []
            seen[temp].append(i)

        for i in seen:
            ans.append([strs[x] for x in seen[i]])

        return ans