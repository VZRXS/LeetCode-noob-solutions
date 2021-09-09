#!/usr/bin/env python3

from sys import path
path.append('.')
from utils.linked_list_utils import LinkedList, ListNode


class Solution(object):
    # 206. Reverse Linked List
    def reverseList(self, head: ListNode) -> ListNode:
        try:
            cur = head.next
            newhead = head
            while cur:
                head.next = cur.next
                cur.next = newhead

                newhead = cur
                cur = head.next
            return newhead
        except:
            return head


if __name__ == '__main__':
    linked_list = [1, 2, 3, 4, 5]
    linked_list_obj = LinkedList()
    head = linked_list_obj.list2LinkedList(input_list=linked_list)
    head = Solution().reverseList(head=head)

    print(linked_list_obj.linkedList2List(head=head))
