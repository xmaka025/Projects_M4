class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Div by 0 was banned")
    return a / b


def operation(e: str) -> float:
    stack = Stack()
    operations = {'+': add, "-": substract, "*": multiply, "/": divide}

    tokens = e.split()

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.push(int(token))
        elif token in operations:
            b = stack.pop()
            a = stack.pop()
            result = operations[token](a, b)
            stack.push(result)

    return stack.pop() if not stack.is_empty() else None


print(operation("3 4 +"))
print(operation("5 1 2 + 4 * + 3 -"))
print(operation("0 4 3 / + 5 / 2 *"))
