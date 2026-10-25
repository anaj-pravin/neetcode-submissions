class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pos_speed)[::-1]:
            if not stack:
                stack.append(((target - p) / s))
                continue
            stack.append((target - p) / s)
            if stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)