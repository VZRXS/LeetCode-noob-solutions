#!/usr/bin/env python3

from sys import path
path.append('.')
from utils.doubly_linked_list_utils import MultilevelNode, MultilevelDoublyLinkedList
Node = MultilevelNode


class Solution(object):
    # 430. Flatten a Multilevel Doubly Linked List
    def flatten(self, head: 'Node') -> 'Node':
        if not head:  # if length == 0
            return head
        cur = head
        head2_parent = None
        while True:
            if cur.child:
                # if current node has child,
                # separate the linked list into two parts: head, head2.
                # head starts from the first node.
                # head2 starts from cur.next (after the node that cur.child exist).
                # then, let cur = cur.child.
                # again, if cur.child exist,
                # update head2 and connect to the previous one.
                # iterate until the whole linked list is traversed
                if cur.next:
                    head2 = cur.next
                    cur2 = head2
                    while cur2.next:
                        cur2 = cur2.next
                    cur2.next = head2_parent
                    try:  # if head2_parent is not None
                        head2_parent.prev = cur2
                    except:
                        pass
                    head2_parent = head2

                cur.next = cur.child
                cur.child = None
                cur.next.prev = cur
            elif cur.next:
                cur = cur.next
            else:
                break
        try:
            cur.next = head2
            head2.prev = cur
            return head
        except:
            return head


if __name__ == '__main__':
    linked_list_obj = MultilevelDoublyLinkedList()
    # multilevel_list = [1,None,2,None,3,None]
    multilevel_list = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, None, None, 11, 12]
    # multilevel_list = []
    head = linked_list_obj.list2LinkedList(input_list=multilevel_list)
    head = Solution().flatten(head=head)

    print(linked_list_obj.FlattenedlinkedList2List(head=head))