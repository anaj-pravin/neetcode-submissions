from operator import add, mul, floordiv, sub
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'-' : sub,'+' : add, '/' : lambda a,b: int(a/b), '*' : mul}

        for i in tokens:
            # print('++++++++++')
            # print(f"stack is {stack}")
            if i in op:
                a = stack.pop()
                b = stack.pop()
                output = op[i](b, a)
                stack.append(output)
                # print(f"output after {b} {i} {a} is {output}")
            else:
                stack.append(int(i))
                # print(f"Appending {i}")

        return stack[0]