#!/usr/bin/env python3
"""
Customized linked list utilities
"""

from typing import List, Optional


class ListNode:
    """
    ListNode class
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    """
    LinkedList class
    """
    def __init__(self):
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

    def list2LinkedList(self, input_list: List) -> Optional[ListNode]:
        """
        Convert list into linked list.
        """
        for val in input_list[::-1]:
            self.addAtHead(val)
        return self.head

    def linkedList2List(self, head: Optional[ListNode]) -> List:
        """
        Convert linked list into list.
        """
        output_list = []
        cur = head
        while cur:
            output_list.append(cur.val)
            cur = cur.next
        return output_list

    def connect2Index(self, head: ListNode, index: int) -> ListNode:
        """
        Connect the last node to the given index.
        """
        if index >= 0:
            tail = head
            while tail.next:
                tail = tail.next
            cur = head
            for _ in range(index):
                cur = cur.next
            tail.next = cur
        return head

    def mergeLists(self, listA: List, listB: List, intersectVal: int, skipA: int,
                   skipB: int) -> ListNode:
        """
        Merge two lists from skipA and skipB.
        """
        if listA[skipA] != intersectVal or listB[skipB] != intersectVal:
            # cannot merge
            headA = LinkedList.list2LinkedList(self, input_list=listA)
            headB = LinkedList.list2LinkedList(self, input_list=listB)
            return headA, headB

        for i in range(skipA, len(listA)):
            if listA[i] != listB[i - skipA + skipB]:
                # cannot merge
                headA = LinkedList.list2LinkedList(self, input_list=listA)
                headB = LinkedList.list2LinkedList(self, input_list=listB)
                return headA, headB

        headA = LinkedList.list2LinkedList(self, input_list=listA)
        headB = LinkedList.list2LinkedList(self, listB[:skipB:])

        curB = headB
        while curB.next:
            curB = curB.next
        curA = headA
        for _ in range(skipA):
            curA = curA.next
        curB.next = curA

        return headA, headB