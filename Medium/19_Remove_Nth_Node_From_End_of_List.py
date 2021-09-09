#!/usr/bin/env python3

from sys import path
path.append('.')
from utils.linked_list_utils import LinkedList, ListNode


class Solution(object):
    # 19. Remove Nth Node From End of List
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        cur = head
        if n > 1:
            for _ in range(length - n):
                cur = cur.next
            cur.val = cur.next.val
            cur.next = cur.next.next
        elif length == 1:
            head = None
        else:
            for _ in range(length - n - 1):
                cur = cur.next
            cur.next = None
        return head

    def removeNthFromEnd_attempt2(self, head: ListNode, n: int) -> ListNode:
        # Two pointers
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if fast:    # if fast is not None
            while fast.next:
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next
        else:   # the last node
            if slow.next:   # if slow.next is not None
                slow.val = slow.next.val
                slow.next = slow.next.next
            else:   # only 1 node
                head = None
        return head


if __name__ == '__main__':
    linked_list_obj = LinkedList()
    linked_list = [1, 2, 3, 4]
    head = linked_list_obj.list2LinkedList(input_list=linked_list)
    # Solution().removeNthFromEnd(head=head, n=2)
    Solution().removeNthFromEnd_attempt2(head=head, n=2)
    
    print(linked_list_obj.linkedList2List(head=head))
