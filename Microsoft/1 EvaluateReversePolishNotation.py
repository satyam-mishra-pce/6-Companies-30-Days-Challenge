class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                stack.append(-stack.pop() + stack.pop())
            elif token == "/":
                op2 = stack.pop()
                op1 = stack.pop()
                ans = abs(op1) // abs(op2)
                if (op1 < 0) ^ (op2 < 0):
                    stack.append(-ans)
                else:
                    stack.append(ans)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(token))
        return stack[0]