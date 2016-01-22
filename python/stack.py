stack = []


def pop():
    if(len(stack) != 0):
        print('Popped value ' + str(stack.pop()))
    else:
        print(' Stack underflow')


def push():
    if(len(stack) + 1 > maxSize):
        print 'Stack Overflow'
    else:
        print('input value to push')
        stack.append(raw_input())
        print stack


operations = {
    'd': pop,
    'i': push
}
maxSize = int(raw_input('Input the size for stack'))
while True:
    print('Options available')
    print('Type:')
    print('i to push')
    print('d to pop')
    print('e to exit')
    option = raw_input()
    if(option == 'e'):
        break

    if option in operations:
        operations[option]()

