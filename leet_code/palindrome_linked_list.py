from collections import deque


def find_pal_linked_list(qu, head):
    if not head:
        return True
    qu.append(head.val)
    # print('qu', qu)
    res = find_pal_linked_list(qu, head.next)
    # print('res head',res, head.val)
    left = qu.popleft()
    if not res or left != head.val:
        # print('qu, head', left, head.val)
        return False
    else:
        return True


def find_if_linked_list_is_palindrome(head):
    return find_pal_linked_list(deque(), head)
