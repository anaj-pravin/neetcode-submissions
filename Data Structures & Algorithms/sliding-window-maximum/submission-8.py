from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        win_ = deque()
        l = r = 0
        n = len(nums)
        res = []

        while r < n:
            while win_ and nums[win_[-1]] < nums[r]:
                win_.pop()

            win_.append(r)

            # print("++++++++")
            # print(f"left = {l}, right = {r}")
            # print(win_)
            # print(f"result = {res}")

            if l > win_[0]:
                win_.popleft()
            
            if (l + r) + 1 >= k:
                res.append(nums[win_[0]])
                l = l + 1
            r += 1

        return res