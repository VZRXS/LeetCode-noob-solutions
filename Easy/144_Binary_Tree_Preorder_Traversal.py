#!/usr/bin/env python3

from typing import List
from sys import path
path.append('.')
from utils.binary_tree_utils import TreeNode


class Solution(object):
    # 144. Binary Tree Preorder Traversal
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Recurse
        output_list = []
        output_list = self.preorderTraverse(root, output_list)
        return output_list

    def preorderTraverse(self, root: TreeNode, output_list: List[int]) -> List[int]:
        if root:
            output_list.append(root.val)
            self.preorderTraverse(root.left, output_list)
            self.preorderTraverse(root.right, output_list)
        return output_list


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, None, TreeNode(3)),
                    TreeNode(4, TreeNode(5), TreeNode(6, TreeNode(7))))
    # root=TreeNode()

    print(Solution().preorderTraversal(root=root))