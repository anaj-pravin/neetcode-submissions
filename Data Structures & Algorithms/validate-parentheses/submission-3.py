class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        in_to_out = {")": "(", "]":"[", "}":"{"}

        for i in range(len(s)):
            if stack and in_to_out.get(s[i], False) and in_to_out[s[i]] == stack[-1]:
                stack.pop()
                continue
            stack.append(s[i])
            # if s[i] in in_to_out.values():
            #     stack.append(s[i])
            # else:
            #     if not stack:
            #         return False

            #     if in_to_out[s[i]] == stack[-1]:
            #         stack.pop()
            #     else:
            #         return False
        if stack:
            return False
        return True