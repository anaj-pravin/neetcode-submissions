class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # print(f"len = {right}, {nums[right]}")
        res = 1001

        while left <= right:
            # print(f"left = {left}, right = {right}")
            mid = (left + right) // 2
            # print(f"mid = {mid}")
            res = min(res, nums[mid])
            if nums[mid] <= nums[right]:
                right = mid - 1
                # res = min(res, nums[mid])
            # elif nums[mid] > nums[right]:
            else:
                left = mid + 1
                # res = min(res, nums[mid])
            # else:
            #     if nums[mid - 1] < nums[mid]:
            #         right = mid - 1
            #         # res = min(res, nums[mid])
            #     else: 
            #         left = mid + 1
                    # res = min(res, nums[mid])
            # print(f"res is {res}")

        return res