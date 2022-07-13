from stack import Stack


stack = Stack()
input_data = ('(((([{}]))))',
              '{{[(])]}}',
              '{{[()]}}',
              '}{}',
              '[([])((([[[]]])))]{()}',
              '[[{())}]')


if __name__ == '__main__':
    for data in input_data:
        print(stack.balance(data))
