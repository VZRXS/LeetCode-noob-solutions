#!/usr/bin/env python3

from typing import List
from sys import path
path.append('.')
from utils.binary_tree_utils import TreeNode


class Solution(object):
    # 104. Maximum Depth of Binary Tree
    def maxDepth(self, root: TreeNode) -> int:
        # Recurse
        depth = self.traverse(root, depth=0)
        return depth

    def traverse(self, root: TreeNode, depth: List[int]) -> List[int]:
        if root:
            depth_l = self.traverse(root.left, depth + 1)
            depth_r = self.traverse(root.right, depth + 1)
            depth = max(depth_l, depth_r)
        return depth

    def maxDepth_attempt2(self, root: TreeNode) -> int:
        # Recurse
        if root:
            return max(
                self.maxDepth_attempt2(root.left) + 1,
                self.maxDepth_attempt2(root.right) + 1)
        return 0


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, None, TreeNode(3)),
                    TreeNode(4, TreeNode(5), TreeNode(6, TreeNode(7))))
    # root=TreeNode()

    print(Solution().maxDepth_attempt2(root=root))