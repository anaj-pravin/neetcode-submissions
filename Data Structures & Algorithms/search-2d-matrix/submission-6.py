class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0]) - 1
        temp = right

        for row in matrix:
            # print("+++++++++++")
            while left <= right:
                mid = (left + right) // 2
                # print(f"left = {left}, right = {right}, mid = {mid}")
                # print(f"row is {row}")
                if row[mid] == target:
                    # print(f"row[mid] = target")
                    return True
                elif row[mid] > target:
                    # print(f"{row[mid]} and {target}")
                    right = mid - 1
                    # print(f"row of mid is {row[mid]}")
                else:
                    left = mid + 1
            # print(f"left = {left}, right = {right}")
            left = 0
            right = temp
        # print("+++++++++")
        # print(f"left = {left}, right = {right}, mid = {mid}")
        return False