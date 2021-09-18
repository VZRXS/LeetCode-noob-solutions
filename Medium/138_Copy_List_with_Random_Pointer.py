#!/usr/bin/env python3

from sys import path
path.append('.')
from utils.doubly_linked_list_utils import RandomNode, RandomLinkedList
Node = RandomNode


class Solution(object):
    # 138. Copy List with Random Pointer
    def copyRandomList(self, head: 'Node') -> 'Node':
        # create a new linked list
        newhead = Node(x=0)
        newcur = newhead
        cur = head
        while cur:
            newcur.next = Node(x=cur.val)
            cur = cur.next
            newcur = newcur.next

        # add random attribute
        # cur: node to add random attribute
        # cur2: node pointed by random attribute
        newcur = newhead.next
        cur = head
        while cur:
            cur2 = head
            newcur2 = newhead.next
            while cur2 is not cur.random:
                cur2 = cur2.next
                newcur2 = newcur2.next
            newcur.random = newcur2
            cur = cur.next
            newcur = newcur.next

        return newhead.next


if __name__ == '__main__':
    random_list_obj = RandomLinkedList()
    # random_list = [[1,1],[2,1]]
    random_list = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    # random_list = []
    # random_list = [[3,None],[3,0],[3,None]]
    head_orig = random_list_obj.list2LinkedList(input_list=random_list)
    head_copy = Solution().copyRandomList(head=head_orig)

    # print(random_list_obj.linkedList2List(head=head_copy))
    print(random_list_obj.deepCopiedLinkedList2List(head_orig=head_orig, head_copy=head_copy))
