#!/usr/bin/env python3

from sys import path
path.append('.')
from utils.linked_list_utils import ListNode

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class MyLinkedList:
    # 707. Design Linked List
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        try:
            if index == 0:
                return self.head.val
            cur = self.head
            for _ in range(index):
                try:  # if cur.next.val exist
                    cur.next.val
                    cur = cur.next
                except:  # invalid index
                    return -1
        except:  # invalid index
            return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newhead = ListNode(val)
        try:
            newhead.next = self.head
        except:  # empty linked list
            newhead.next = None
        self.head = newhead

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newtail = ListNode(val)
        prev = self.head
        try:
            while prev.next is not None:
                prev = prev.next
            prev.next = newtail
        except:  # empty linked list
            self.head = newtail
            self.head.next = None

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        newnode = ListNode(val)
        try:
            if index == 0:
                newnode.next = self.head
                self.head = newnode
            else:
                prev = self.head
                for _ in range(index - 1):
                    prev = prev.next
                newnode.next = prev.next
                prev.next = newnode
        except:  # invalid index
            return

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        prev = self.head
        if index == 0:
            try:
                self.head.val = self.head.next.val
                self.head.next = self.head.next.next
            except:
                self.head = None
        else:
            try:
                for _ in range(index - 1):
                    prev = prev.next
                prev.next = prev.next.next
            except:
                return


if __name__ == '__main__':
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    param_1 = obj.get(1)
    obj.deleteAtIndex(1)
    param_2 = obj.get(1)

    print(param_1, param_2)
