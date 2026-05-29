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


def valid_bracket(s: str) -> bool:
    bracket = {')': '(', '}': '{', ']': '['}
    stack = Stack()

    for open_br in s:
        if open_br in '({[':
            stack.push(open_br)
        elif open_br in ')}]':
            ls_open = stack.pop()
            if ls_open != bracket[open_br]:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    test = ["([]{})", "([)]", "{[}]", "()"]

    for test in test:
        result = "Right" if valid_bracket(test) else "Wrong"
        print(f"The line '{test}' is  {result}")
