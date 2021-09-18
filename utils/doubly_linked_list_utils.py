#!/usr/bin/env python3
"""
Customized doubly linked list utilities
"""

from typing import List, Optional, Union


class DoublyNode:
    """
    Doubly linked list node class
    """
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MultilevelNode:
    """
    Multilevel doubly linked list node class
    """
    def __init__(self,
                 val: int = 0,
                 prev: 'MultilevelNode' = None,
                 next: 'MultilevelNode' = None,
                 child: 'MultilevelNode' = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class RandomNode:
    def __init__(self, x: int, next: 'RandomNode' = None, random: 'RandomNode' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class MultilevelDoublyLinkedList:
    """
    Multilevel doubly linked list class
    """
    def __init__(self):
        self.head = None

    def addFirstNode(self, val: int) -> None:
        """
        Add the first node of the linked list.
        """
        newhead = MultilevelNode(val)
        try:
            newhead.next = self.head
        except:  # empty linked list
            newhead.next = None
        self.head = newhead

    def addAtTail(self, head: MultilevelNode, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newtail = MultilevelNode(val)
        prev = head
        try:
            while prev.next is not None:
                prev = prev.next
            prev.next = newtail
            prev.next.prev = prev
        except:  # empty linked list
            head = newtail
            head.next = None

    def addChild2Index(self, head: MultilevelNode, head_child: MultilevelNode,
                       index: int) -> MultilevelNode:
        cur = head
        for _ in range(index):
            cur = cur.next
        cur.child = head_child
        return head

    def list2LinkedList(self, input_list: List) -> Optional[MultilevelNode]:
        """
        Convert list into multilevel doubly linked list.
        """
        try:
            self.addFirstNode(val=input_list[0])
        except:
            return self.head
        head_parent = self.head
        fast = 1
        slow = 0
        while fast < len(input_list):
            if input_list[fast] is None and input_list[slow] is not None:
                slow = fast
            elif input_list[fast] is not None and input_list[slow] is None:
                head_child = MultilevelNode(val=input_list[fast])
                self.addChild2Index(head=head_parent, head_child=head_child, index=fast - slow - 1)
                head_parent = head_child
                slow = fast
            elif input_list[fast] is not None and input_list[slow] is not None:
                self.addAtTail(head=head_parent, val=input_list[fast])
            fast += 1
        return self.head

    def linkedList2List(self, head: Optional[MultilevelNode]) -> Optional[List]:
        """
        Convert multilevel doubly linked list into list.
        """
        output_list = []
        cur = head
        newhead = None
        index = 0
        while cur:
            if cur.child:
                newhead = cur.child
            output_list.append(cur.val)
            cur = cur.next
            if not newhead:
                index += 1
            if newhead and not cur:
                cur = newhead
                newhead = None
                for _ in range(index + 1):
                    output_list.append(None)
                index = 0
        return output_list

    def flattenCheck(self, head: Optional[MultilevelNode]) -> bool:
        """
        Check whether it is a valid flattened doubly linked list
        """
        cur = head
        while cur:
            if cur.child:
                return False
            cur = cur.next
        return True

    def FlattenedlinkedList2List(self, head: Optional[MultilevelNode]) -> Union[List, str]:
        """
        Convert flattened multilevel doubly linked list into list.
        """
        output_list = []
        cur = head
        while cur:
            output_list.append(cur.val)
            cur = cur.next
        if self.flattenCheck(head=head):
            return output_list
        return f"The linked list {output_list} is not a valid doubly linked list."


class RandomLinkedList:
    """
    Random singly linked list class
    """
    def __init__(self):
        self.head = None

    def addFirstNode(self, val: int) -> None:
        """
        Add the first node of the linked list.
        """
        newhead = RandomNode(val)
        try:
            newhead.next = self.head
        except:  # empty linked list
            newhead.next = None
        self.head = newhead

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newtail = RandomNode(val)
        prev = self.head
        try:
            while prev.next is not None:
                prev = prev.next
            prev.next = newtail
        except:  # empty linked list
            self.head = newtail
            self.head.next = None

    def list2LinkedList(self, input_list: List) -> Optional[RandomNode]:
        """
        Convert list into random doubly linked list.
        """
        for node in input_list:
            self.addAtTail(val=node[0])
        cur = self.head
        for node in input_list:
            randomhead = self.head
            try:
                for _ in range(node[1]):
                    randomhead = randomhead.next
            except:
                randomhead = None
            cur.random = randomhead
            cur = cur.next
            randomhead = self.head
        return self.head

    def linkedList2List(self, head: Optional[RandomNode]) -> List:
        """
        Convert random doubly linked list into list.
        """
        output_list = []
        cur = head
        while cur:
            cur2 = head
            index = 0
            if cur.random:
                while cur2 is not cur.random:
                    cur2 = cur2.next
                    index += 1
            else:
                index = None
            output_list.append([cur.val, index])
            cur = cur.next
        return output_list

    def deepCopiedLinkedList2List(self, head_orig: Optional[RandomNode],
                                  head_copy: Optional[RandomNode]) -> Union[List, str]:
        """
        Check deep copy and convert random doubly linked list into list.
        """
        cur_orig = head_orig
        cur_copy = head_copy
        while cur_orig:
            if cur_copy is cur_orig:
                return f"Node with label {cur_copy.val} was not copied but a reference to the original one."
            cur_orig = cur_orig.next
            cur_copy = cur_copy.next
        return self.linkedList2List(head=head_copy)