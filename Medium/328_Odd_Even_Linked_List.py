#!/usr/bin/env python3

from sys import path
path.append('.')
from utils.linked_list_utils import LinkedList, ListNode


class Solution(object):
    # 328. Odd Even Linked List
    def oddEvenList(self, head: ListNode) -> ListNode:
        try:
            head.next.next.val  # if length >= 3
            odd = head
            even = head.next
            evenhead = head.next
        except:
            return head

        # demonstration:
        #
        # 1-2-3-4-5-None
        #
        # 1-3-4-5-None
        #  2-/
        #
        # 1-3-5-None
        #  2-4-/
        #
        # 1-3-5-\  /-None
        #       2-4

        while odd.next and even.next:
            odd.next = even.next
            odd = even.next

            even.next = odd.next
            even = odd.next

        odd.next = evenhead  # link the last odd node to the first even node
        return head


if __name__ == '__main__':
    linked_list = [1, 2, 3, 4, 5]
    linked_list_obj = LinkedList()
    head = linked_list_obj.list2LinkedList(input_list=linked_list)
    head = Solution().oddEvenList(head=head)

    print(linked_list_obj.linkedList2List(head=head))
