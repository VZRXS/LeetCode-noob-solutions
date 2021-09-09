#!/usr/bin/env python3

from sys import path
path.append('.')
from utils.linked_list_utils import LinkedList, ListNode


class Solution(object):
    # 160. Intersection of Two Linked Lists
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # OVERTIME
        curA = headA
        curB = headB
        while curB:
            while curA:
                if curA is curB:
                    return f'Intersected at {curA.val}'  # for local debugging
                    return curA
                curA = curA.next
            curB = curB.next
            curA = headA
        return 'No intersection'  # for local debugging
        return

    def getIntersectionNode_attempt2(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA = headA
        curB = headB
        lenA = 0
        lenB = 0
        # get length
        while curA:
            curA = curA.next
            lenA += 1
        while curB:
            curB = curB.next
            lenB += 1

        curA = headA
        curB = headB

        # arrange the start index
        # to let their length of the rest same
        # s: start, t: terminal, i: identical
        # O-O-(s)-O\
        #           O-O-O-(t)
        #     (s)-O/
        if lenA <= lenB:
            startA = 0
            startB = lenB - lenA
            for _ in range(startB):
                curB = curB.next
        else:
            startB = 0
            startA = lenA - lenB
            for _ in range(startA):
                curA = curA.next

        # stop when nodeA and nodeB are identical
        # O-O-O-O\
        #        (i)-O-O-(t)
        #     O-O/
        while curA:
            if curA is curB:
                return curA
            curA = curA.next
            curB = curB.next
        return


if __name__ == '__main__':
    listA = [1, 2, 3, 4, 5]
    listB = [-1, 0, 1, 2, 3, 4, 5]
    intersectVal = 2
    skipA = 1
    skipB = 3
    linked_list_obj = LinkedList()
    headA, headB = linked_list_obj.mergeLists(listA=listA,
                                              listB=listB,
                                              intersectVal=intersectVal,
                                              skipA=skipA,
                                              skipB=skipB)
    # head = Solution().getIntersectionNode(headA=headA, headB=headB)
    head = Solution().getIntersectionNode_attempt2(headA=headA, headB=headB)

    if head:
        print(f'Intersected at {head.val}')
    else:
        print('No intersection')
