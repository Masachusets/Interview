class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return not bool(self.stack)

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def balance(self, balance_string: str):
        self.stack = []
        for i in balance_string:
            if i in '({[':
                self.push(i)
            elif i in ')}]':
                if self.isEmpty():
                    return "Несбалансированно"
                last_elem = self.pop()
                if last_elem == '(' and i == ')':
                    continue
                elif last_elem == '{' and i == '}':
                    continue
                elif last_elem == '[' and i == ']':
                    continue
                else:
                    return "Несбалансированно"
        if self.isEmpty():
            return "Сбалансированно"
        else:
            return "Несбалансированно"
