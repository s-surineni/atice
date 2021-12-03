def reverse_ll(head):
    prev = None
    temp, curr = head, head
    while curr:
        # print(curr.val)
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def find_if_linked_list_is_palindrome(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # print("*" * 80)
    # print("ironman slow.val", slow.val)
    head2 = reverse_ll(slow)
    # print(head2.val, "head2")
    while head2:
        print("h h2", head.val, head2.val)
        if head.val != head2.val:
            return False
        head = head.next
        head2 = head2.next
    return True
