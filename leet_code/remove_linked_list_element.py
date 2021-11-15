# https://leetcode.com/problems/remove-linked-list-elements/
def remove_linked_list_element(head, val):
    while head and head.val == val:
        head = head.next
    curr = head
    # print('head', head.val)
    while curr and curr.next:
        while curr.next and curr.next.val == val:
            curr.next = curr.next.next

        curr = curr.next
    return head
