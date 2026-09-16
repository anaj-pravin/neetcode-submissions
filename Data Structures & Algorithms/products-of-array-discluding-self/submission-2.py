class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left = []
        right = []
        n = len(nums)
        before = None

        for i in range(n):
            if before == None:
                left.append(1)
                before = 1
            else:
                before = before * nums[i - 1]
                left.append(before)

        before = None

        for i in range(n-1,-1,-1):
            if before == None:
                right.append(1)
                before = nums[i]
            else:
                right.append(before)
                before = before * nums[i]

        for i in range(n):
            output.append(left[i] * right[n - 1 - i])
        return output




