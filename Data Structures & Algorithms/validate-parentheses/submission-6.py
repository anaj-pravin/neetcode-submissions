class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        in_to_out = {")": "(", "]":"[", "}":"{"}

        for i in s:
            if i in in_to_out:
                if stack and stack[-1] == in_to_out[i]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(i)
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