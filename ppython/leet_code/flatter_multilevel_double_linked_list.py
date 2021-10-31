# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
def flatten_multi_level_linked_list(head):

    stack = []
    curr = head
    if not head:
        return
    while stack or curr:
        #         print('curr', curr.val)
        #         if curr.next: print('next', curr.next.val)

        #         if curr.child: print('child', curr.child.val)
        if curr.child:
            if curr.next:
                stack.append(curr.next)
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
            curr = curr.next
        elif not curr.next and stack:
            temp = stack.pop()
            curr.next = temp
            temp.prev = curr
            curr = temp
        else:
            curr = curr.next
    return head
