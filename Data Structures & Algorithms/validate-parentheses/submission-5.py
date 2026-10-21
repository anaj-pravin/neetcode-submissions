class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        in_to_out = {")": "(", "]":"[", "}":"{"}

        for i in s:
            if i in in_to_out.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                # print(in_to_out[s[i]] == stack[-1])
                if in_to_out[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True