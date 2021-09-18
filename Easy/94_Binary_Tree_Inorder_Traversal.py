#!/usr/bin/env python3

from typing import List
from sys import path
path.append('.')
from utils.binary_tree_utils import TreeNode


class Solution(object):
    # 94. Binary Tree Inorder Traversal
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # Recurse
        output_list = []
        output_list = self.inorderTraverse(root, output_list)
        return output_list

    def inorderTraverse(self, root: TreeNode, output_list: List[int]) -> List[int]:
        if root:
            self.inorderTraverse(root.left, output_list)
            output_list.append(root.val)
            self.inorderTraverse(root.right, output_list)
        return output_list


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, None, TreeNode(3)),
                    TreeNode(4, TreeNode(5), TreeNode(6, TreeNode(7))))
    # root=TreeNode()

    print(Solution().inorderTraversal(root=root))