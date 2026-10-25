class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [[p, s] for p, s in zip(position, speed)]
        stack = []
        pos_speed.sort(reverse = True)
        stack.append(((target - pos_speed[0][0]) / pos_speed[0][1]))
        count = 1

        for p, s in pos_speed[1::]:
            # print("postion , speed")
            # print(p, s)
            time = (target - p) / s
            # print(time)
            if stack[-1] >= time:
                # print("Treu")
                continue
            count += 1
            stack.append(time)

        return count