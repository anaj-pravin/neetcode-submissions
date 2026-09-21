class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = 0
        temp = 0
        nums = set(nums)

        for num in nums:
            if num - 1 in nums:
                continue
            temp += 1

            while True:
                if (num + 1) in nums:
                    print(num)
                    temp += 1
                    num = num + 1
                else:
                    break
            if temp > seq:
                seq = temp
            temp = 0
        
        return seq