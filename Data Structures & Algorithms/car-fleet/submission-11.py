class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position, speed), reverse=True)
        stack = (target - pos_speed[0][0]) / pos_speed[0][1]
        # stack.append(((target - pos_speed[0][0]) / pos_speed[0][1]))
        count = 1

        for p, s in pos_speed:
            time = (target - p) / s
            if stack >= time:
                continue
            count += 1
            stack = time

        return count