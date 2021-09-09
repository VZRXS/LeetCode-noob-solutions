#!/usr/bin/env python3

from sys import path
path.append('.')
from utils.linked_list_utils import LinkedList, ListNode


class Solution(object):
    # 142. Linked List Cycle II
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        try:
            while slow.next.val is not None:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    break
        except:
            return 'no cycle'   # for local debugging
            return

        index = 0   # for local debugging
        while head is not slow: # assign a new slow pointer from the head
            head = head.next
            slow = slow.next
            index += 1  # for local debugging
        return f'tail connects to node index {index}'   # for local debugging
        return head


if __name__ == '__main__':
    linked_list_obj = LinkedList()
    linked_list = [1, 2, 3, 4]
    head = linked_list_obj.list2LinkedList(input_list=linked_list)
    head = linked_list_obj.connect2Index(head=head, index=1)

    print(Solution().detectCycle(head=head))