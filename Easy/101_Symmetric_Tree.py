#!/usr/bin/env python3

from sys import path
path.append('.')
from utils.binary_tree_utils import TreeNode


class Solution(object):
    # 101. Symmetric Tree
    def isSymmetric(self, root: TreeNode) -> bool:
        # Idea: level order traversal
        queue = [root]
        cur_level = []
        while queue:
            for _ in range(len(queue)):
                if queue[_] is not None:
                    cur_level.append(queue[_].val)
                    queue.append(queue[_].left)
                    queue.append(queue[_].right)
                else:
                    cur_level.append(None)

            for i in range(len(cur_level) // 2):
                if cur_level[i] != cur_level[-1 - i]:
                    return False
            queue = [node for node in queue[_ + 1::]]
            cur_level = []

        return True


if __name__ == '__main__':
    # root=TreeNode(1,TreeNode(2,None,TreeNode(3)),TreeNode(4,TreeNode(5),TreeNode(6,TreeNode(7))))
    # root = TreeNode(1, TreeNode(2))
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)),
                    TreeNode(2, TreeNode(3), TreeNode(4)))
    # root=TreeNode()

    print(Solution().isSymmetric(root=root))