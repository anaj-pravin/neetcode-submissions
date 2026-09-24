class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(numbers)):
            c = target - numbers[i]
            if numbers[i] in seen:
                return [seen[numbers[i]], i + 1]
            seen[c] = i + 1
        
        return 