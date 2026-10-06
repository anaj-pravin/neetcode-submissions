class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        output = 0

        while(left < right):
            h = min(heights[left], heights[right]) * (right- left)

            if h > output:
                output = h
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1     

        return output