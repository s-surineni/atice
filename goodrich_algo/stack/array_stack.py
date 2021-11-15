class ArrayStack:

    def __init__(self):
        self.stack = [None] * 10
        self.top = -1
        self.capacity = 10

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

    def top_ele(self):
        return self.stack(self.top)

    def pop(self):
        if self.top == -1:
            return "stack empty"
        else:
            top = self.stack[self.top]
            self.top -= 1
            return top

    def push(self, ele):
        if self.top == (self.capacity - 1):
            return "stack is full"
        else:
            self.top += 1
            self.stack[self.top] = ele

    def output(self):
        print(self.stack)


stack = ArrayStack()


def pusher():
    ele = int(input('enter element to push: '))
    print()
    stack.push(ele)


if __name__ == '__main__':
    menu = {
        'e': stack.is_empty,
        's': stack.size,
        't': stack.top_ele,
        'p': stack.pop,
        'pu': pusher,
        'o': stack.output
    }


    while(True):
        print('e: stack.is_empty,')
        print('s: stack.size,')
        print('t: stack.top_ele,')
        print('p: stack.pop,')
        print('pu: stack.push,')
        print('o: stack.output')

        choice = input('please choose one of the above choice: ')
        if choice == 'x':
            break
        menu[choice]()
