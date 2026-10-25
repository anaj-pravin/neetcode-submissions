class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [[p, s] for p, s in zip(position, speed)]
        stack = []
        pos_speed.sort(reverse = True)
        stack.append(((target - pos_speed[0][0]) / pos_speed[0][1]))
        # print(pos_speed[0][1])
        count = len(speed) + 1
        for p, s in pos_speed:
            stack.append((target - p) / s)
            if stack[-1] <= stack[-2]:
                stack.pop()
                count -= 1

        return count