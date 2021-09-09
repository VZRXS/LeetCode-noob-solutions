#!/usr/bin/env python3

from sys import path
path.append('.')
from utils.linked_list_utils import LinkedList, ListNode


class Solution(object):
    # 21. Merge Two Sorted Lists
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:  # l1, l2 != None
            if l1.val <= l2.val:
                head = l1
                l1 = l1.next
            else:
                head = l2
                l2 = l2.next
            cur = head
            while l1 or l2:
                try:
                    if l1.val <= l2.val:
                        cur.next = l1
                        cur = cur.next
                        l1 = l1.next
                    else:
                        cur.next = l2
                        cur = cur.next
                        l2 = l2.next
                except:
                    if l1:
                        while l1:
                            cur.next = l1
                            cur = cur.next
                            l1 = l1.next
                    else:
                        while l2:
                            cur.next = l2
                            cur = cur.next
                            l2 = l2.next
            return head
        elif l1:  # l1 != None
            return l1
        else:  # l1 == None
            return l2

    def mergeTwoLists_attempt2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:  # l1, l2 != None
            head = ListNode()  # create an empty head
            cur = head
            while l1 or l2:
                try:
                    if l1.val <= l2.val:
                        cur.next = l1
                        cur = cur.next
                        l1 = l1.next
                    else:
                        cur.next = l2
                        cur = cur.next
                        l2 = l2.next
                except:
                    if l1:
                        while l1:
                            cur.next = l1
                            cur = cur.next
                            l1 = l1.next
                    else:
                        while l2:
                            cur.next = l2
                            cur = cur.next
                            l2 = l2.next
            head = head.next  # delete empty head
            return head
        elif l1:  # l1 != None
            return l1
        else:  # l1 == None
            return l2


if __name__ == '__main__':
    linked_list1 = [1, 1, 3]
    linked_list2 = [0, 1, 3]
    linked_list_obj = LinkedList()
    l1 = linked_list_obj.list2LinkedList(input_list=linked_list1)
    l2 = linked_list_obj.list2LinkedList(input_list=linked_list2)
    # head = Solution().mergeTwoLists(l1=l1, l2=l2)
    head = Solution().mergeTwoLists_attempt2(l1=l1, l2=l2)

    print(linked_list_obj.linkedList2List(head=head))
