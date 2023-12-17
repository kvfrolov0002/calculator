class Calculator:
    def __init__(self):
        pass

    def num_operations(self, x, y, operator):
        ops = {'+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '*': lambda x, y: x * y,
               '/': lambda x, y: x / y if y != 0 else None}
        if ops[operator](x, y) is None:
            raise ValueError("Ошибка, деление на нуль")
        return ops[operator](x, y)

    def order(self, first, second):
        return {'+': 1, '-': 1, '*': 2, '/': 2}[first] >= {'+': 1, '-': 1, '*': 2, '/': 2}[second]

    def evaluate(self, problem):
        digits, operations, i, nums = [], [], 0, len(problem)
        while i < nums:
            if problem[i] in {'+': 1, '-': 1, '*': 2, '/': 2}:
                while operations and operations[-1] != '(' and self.order(operations[-1], problem[i]):
                    y, x = digits.pop(), digits.pop()
                    res = self.num_operations(x, y, operations.pop())
                    digits.append(res)
                add_value = problem[i]
                operations.append(add_value)

            elif problem[i] == '(':
                add_value = problem[i]
                operations.append(add_value)
            elif problem[i] == ')':
                while operations and operations[-1] != '(':
                    y, x = digits.pop(), digits.pop()
                    res = self.num_operations(x, y, operations.pop())
                    digits.append(res)
                operations.pop()
            elif problem[i].isdigit() or problem[i] == '.':
                num = str()
                while i < len(problem) and (problem[i].isdigit() or problem[i] == '.'):
                    add_value = problem[i]
                    num += add_value
                    i += 1

                i -= 1
                digits.append(float(num))
            i += 1

        while operations:
            y, x = digits.pop(), digits.pop()
            res = self.num_operations(x, y, operations.pop())
            digits.append(res)

        return digits[-1]

