#!/usr/bin/env python3

from sys import path
path.append('.')
from utils.linked_list_utils import LinkedList, ListNode


class Solution(object):
    # 234. Palindrome Linked List
    def isPalindrome(self, head: ListNode) -> bool:
        temp_list = []
        while head:
            temp_list.append(head.val)
            head = head.next
        for i in range(len(temp_list) // 2):
            if temp_list[i] != temp_list[-1 - i]:
                return False
        return True

    def isPalindrome_attempt2(self, head: ListNode) -> bool:
        # Two pointers
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        if length > 1:
            cur = head.next
            newhead = head

            # reverse the first half part
            for _ in range(length // 2 - 1):
                head.next = cur.next
                cur.next = newhead

                newhead = cur
                cur = head.next

            # move mid pointer forward, if the length is an odd number
            # not need to consider the middle node
            if length % 2 == 1:
                mid = cur.next
            else:
                mid = cur

            # compare head and mid
            while mid:
                if newhead.val != mid.val:
                    return False
                newhead = newhead.next
                mid = mid.next
            return True
        else:  # length <= 1
            return True


if __name__ == '__main__':
    linked_list = [1, 2, 2, 1]
    linked_list_obj = LinkedList()
    head = linked_list_obj.list2LinkedList(input_list=linked_list)

    # print(Solution().isPalindrome(head=head))
    print(Solution().isPalindrome_attempt2(head=head))
