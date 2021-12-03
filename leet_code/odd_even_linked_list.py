def odd_even_linked_list(head):
    if not head:
        return None
    # odd_head = head
    odd = head
    even_head = head.next
    even = even_head
    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next
    odd.next = even_head
    return head
