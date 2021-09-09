#!/usr/bin/env python3

from sys import path
path.append('.')
from utils.linked_list_utils import LinkedList, ListNode


class Solution(object):
    # 203. Remove Linked List Elements
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        try:  # delete nodes that head.val==val from head
            while head.val == val:
                head.val = head.next.val
                head.next = head.next.next
        except:  # only one node is left
            head = None
            return head

        cur = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


if __name__ == '__main__':
    linked_list = [3, 3, 3, 3]
    linked_list_obj = LinkedList()
    head = linked_list_obj.list2LinkedList(input_list=linked_list)
    head = Solution().removeElements(head=head, val=3)

    print(linked_list_obj.linkedList2List(head=head))
