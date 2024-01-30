class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: b - a,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(b / a)
        }
        for token in tokens:
            if token in operations:
                operand_one, operand_two = stack.pop(), stack.pop()
                operation = operations[token]
                stack.append(operation(operand_one, operand_two))
            else:
                stack.append(int(token))
        return stack[0]