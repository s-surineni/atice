import sys

queue = [None] * 3
print (queue)
head = tail = 0
qLen = 3


def deQueue():
    global head
    if head == tail:
        print ('Underflow')
    else:
        print (queue[head])
        head += 1
        head %= qLen


def enQueue():
    global tail
    if (tail + 1) % qLen == head:
        print ('Queue Overflow', file=sys.stderr)
    else:
        print('input value to en-queue')
        queue[tail] = input()
        tail += 1
        tail %= qLen
        print (queue)


operations = {
    'd': deQueue,
    'i': enQueue
}

while True:
    print('Options available')
    print('Type:')
    print('i to en-queue')
    print('d to de-queue')
    print('e to exit')
    option = input()
    if(option == 'e'):
        break

    if option in operations:
        operations[option]()
