class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+", "-", "/", "*"}
        final = 0
        if len(tokens) < 2:
            return int(tokens[0])

        for token in range(len(tokens)):
            if tokens[token] not in operands:
                stack.append(tokens[token])
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                operand = tokens[token]
                if operand == "+":
                    final = (num1 + num2)
                elif operand == "-":
                    final = (num1 - num2)
                elif operand == "*":
                    final = (num1 * num2)
                else:
                    final = (num1 // num2)
                    if final < 0 and num1%num2 != 0:
                        final += 1
                stack.append(final)
        return final