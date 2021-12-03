def find_if_cycle(head):
    slow, fast = [head] * 2
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    else:
        return False
