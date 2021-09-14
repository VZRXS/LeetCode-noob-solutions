#!/usr/bin/env python3

from sys import path
path.append('.')
from utils.linked_list_utils import LinkedList, ListNode


class Solution(object):
    # 2. Add Two Numbers
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        head = l3
        while l1 and l2:
            if l3.val + l1.val + l2.val >= 10:
                l3.val = (l3.val + l1.val + l2.val) % 10
                l3.next = ListNode(val=1)
            else:
                l3.val += l1.val + l2.val
                l3.next = ListNode()
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        if l2:
            l1 = l2
        while l1:
            if l3.val + l1.val == 10:
                l3.val = 0
                l3.next = ListNode(val=1)
            else:
                l3.val += l1.val
                l3.next = ListNode()

            l3 = l3.next
            l1 = l1.next

        if l3.val == 0:
            prev = head
            while prev.next.next:
                prev = prev.next
            prev.next = None

        return head


if __name__ == '__main__':
    l1 = [9, 9, 9]
    l2 = [9, 9, 9, 9, 9, 9]
    linked_list_obj = LinkedList()
    head1 = linked_list_obj.list2LinkedList(input_list=l1)
    head2 = linked_list_obj.list2LinkedList(input_list=l2)
    head = Solution().addTwoNumbers(l1=head1, l2=head2)

    print(linked_list_obj.linkedList2List(head=head))