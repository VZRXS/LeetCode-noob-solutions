#!/usr/bin/env python3

from sys import path
path.append('.')
from utils.linked_list_utils import LinkedList


class Solution(object):
    # 237. Delete Node in a Linked List
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    linked_list_obj = LinkedList()
    linked_list = [1, 2, 3, 4, 5]
    head = linked_list_obj.list2LinkedList(input_list=linked_list)
    node2delete = head.next.next
    Solution().deleteNode(node=node2delete)
    
    print(linked_list_obj.linkedList2List(head=head))
