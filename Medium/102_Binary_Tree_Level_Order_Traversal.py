#!/usr/bin/env python3

from typing import List
from sys import path
path.append('.')
from utils.binary_tree_utils import TreeNode


class Solution(object):
    # 102. Binary Tree Level Order Traversal
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # DOES NOT OUTPUT IN THE RIGHT ORDER
        if root is None:
            return []
        queue = [root]
        trav_result = []
        while queue:
            trav_result.append([node.val for node in queue if node is not None])
            next_level = [
                node.left for node in queue if node is not None and node.left is not None
            ] + [node.right for node in queue if node is not None and node.right is not None]
            queue = next_level
        return trav_result

    def levelOrder_attempt2(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        trav_result = []
        while queue:
            trav_result.append([node.val for node in queue])
            for i in range(len(queue)):
                if queue[i] is not None:
                    queue.append(queue[i].left)
                    queue.append(queue[i].right)
            queue = [node for node in queue[i + 1::] if node is not None]
        return trav_result


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, None, TreeNode(3)),
                    TreeNode(4, TreeNode(5), TreeNode(6, TreeNode(7))))
    # root=TreeNode()

    print(Solution().levelOrder_attempt2(root=root))
    from time import time
    t=time()
    for _ in range(10000):
        # code to test
        Solution().levelOrder_attempt2(root=root)
    print(time()-t)