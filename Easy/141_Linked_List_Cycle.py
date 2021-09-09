#!/usr/bin/env python3

from sys import path
path.append('.')
from utils.linked_list_utils import LinkedList, ListNode


class Solution(object):
    # 141. Linked List Cycle
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        try:
            while slow.next:  # while slow.next is not None
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
        except:
            return False


if __name__ == '__main__':
    linked_list_obj = LinkedList()
    linked_list = [1, 2, 3, 4]
    head = linked_list_obj.list2LinkedList(input_list=linked_list)
    head = linked_list_obj.connect2Index(head=head, index=1)

    print(Solution().hasCycle(head=head))
