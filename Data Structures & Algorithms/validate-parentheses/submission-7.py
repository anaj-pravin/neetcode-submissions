class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        in_to_out = {")": "(", "]":"[", "}":"{"}

        for i in s:
            if i in in_to_out:
                if stack and stack[-1] == in_to_out[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if stack:
            return False
        return True