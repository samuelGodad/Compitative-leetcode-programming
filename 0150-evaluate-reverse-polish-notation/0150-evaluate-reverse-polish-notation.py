from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                operand_one, operand_two = stack.pop(), stack.pop()
                stack.append(operand_one + operand_two)
            elif token == "-":
                operand_one, operand_two = stack.pop(), stack.pop()
                stack.append(operand_two - operand_one)
            elif token == "*":
                operand_one, operand_two = stack.pop(), stack.pop()
                stack.append(operand_one * operand_two)
            elif token == "/":
                operand_one, operand_two = stack.pop(), stack.pop()
                stack.append(int(operand_two / operand_one))
            else:
                stack.append(int(token))
        return stack[0]