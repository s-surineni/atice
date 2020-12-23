def find_if_circular(lin_node):
    fast = slow = lin_node
    while slow:
        slow = slow.next
        if fast.next:
            fast = fast.next.next
        else:
            print('This is not a circular list')
            break
        if slow == fast:
            print('This is a circular list')
            break
    else:
        print('This is not a circular list')



# 1 2 3
