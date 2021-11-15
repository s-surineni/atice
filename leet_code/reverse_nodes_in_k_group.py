class ListNode:
    def __init__(self, v, next=None):
        self.v = v
        self.next = next


def construct_linked_list(num_list):
    head = ListNode(num_list[0])
    curr = head
    idx = 1
    while idx < len(num_list):
        curr.next = ListNode(num_list[idx])
        curr = curr.next
        idx += 1
    return head


def print_ll(head):
    curr = head
    while curr:
        print(curr.v, end=' ')
        curr = curr.next
    print()


def reverseKGroup(head, k):
    dummy = jump = ListNode(0)
    dummy.next = l = r = head

    while True:
        count = 0
        while r and count < k:   # use r to locate the range
            r = r.next
            count += 1
        if count == k:  # if size k satisfied, reverse the inner linked list
            pre, cur = r, l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur  # standard reversing
            jump.next, jump, l = pre, l, r  # connect two k-groups
        else:
            return dummy.next


num_list = [1, 2, 3, 4, 5, 6, 7]
head = construct_linked_list(num_list)
print_ll(head)
reverseKGroup(head, 3)
print_ll(head)
