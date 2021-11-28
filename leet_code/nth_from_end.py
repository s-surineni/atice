# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
def remove_nth_from_end(head, nth):
    n1, n2 = head, head

    for _ in range(nth):
        if not n2.next:
            return n1.next
        n2 = n2.next

    while n2.next:
        n1 = n1.next
        n2 = n2.next

    n1.next = n1.next.next
    return head
