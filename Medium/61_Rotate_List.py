#!/usr/bin/env python3

from typing import Optional
from sys import path
path.append('.')
from utils.linked_list_utils import LinkedList, ListNode


class Solution(object):
    # 61. Rotate List
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        try:  # get length & close the list into a cycle
            cur = head.next
            length = 2
            while cur.next:
                cur = cur.next
                length += 1
            cur.next = head
        except:  # length <= 1
            return head

        # get new head
        index = length - k % length
        for _ in range(index):
            head = head.next

        # break the cycle
        cur = head
        for _ in range(length - 1):
            cur = cur.next
        cur.next = None

        return head


if __name__ == '__main__':
    linked_list_obj = LinkedList()
    linked_list = [0, 1, 2, 3]
    head = linked_list_obj.list2LinkedList(input_list=linked_list)
    head = Solution().rotateRight(head=head, k=6)

    print(linked_list_obj.linkedList2List(head=head))