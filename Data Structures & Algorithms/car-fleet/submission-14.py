class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = {position[i] : speed[i] for i in range(len(speed))}
        pos_speed_sorted = sorted(pos_speed, reverse = True)
        stack = (target - pos_speed_sorted[0]) / pos_speed[pos_speed_sorted[0]]
        # stack.append(((target - pos_speed[0][0]) / pos_speed[0][1]))
        count = 1

        for p in pos_speed_sorted:
            time = (target - p) / pos_speed[p]
            if stack >= time:
                continue
            count += 1
            stack = time

        return count