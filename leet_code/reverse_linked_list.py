# https://leetcode.com/problems/reverse-linked-list/
def reverse(curr):
    if not curr.next:
        return curr, curr
    temp = curr.next
    curr.next = None
    res, head = reverse(temp)
    res.next = curr
    return curr, head


"""
class Solution:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    return self._reverse(head)

def _reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)
"""

reverse(head)
