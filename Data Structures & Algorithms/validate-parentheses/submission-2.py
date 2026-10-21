class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        in_to_out = {")": "(", "]":"[", "}":"{"}

        for i in range(len(s)):
            if s[i] in in_to_out.values():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                # print(in_to_out[s[i]] == stack[-1])
                if in_to_out[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
        # print(s[1])
        # print(s[1] == in_to_out)
        # print(stack)