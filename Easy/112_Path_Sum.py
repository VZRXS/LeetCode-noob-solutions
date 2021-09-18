#!/usr/bin/env python3

from typing import List, Optional
from sys import path
path.append('.')
from utils.binary_tree_utils import TreeNode


class Solution(object):
    # 112. Path Sum
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Recurse
        return self.traverse(root=root, targetSum=targetSum, flag=False)

    def traverse(self, root: TreeNode, targetSum: int, flag: bool) -> List[int]:
        if root:
            if root.val == targetSum and not (root.left or root.right):
                flag = True
            else:
                flag = self.traverse(root.left, targetSum - root.val, flag)
                flag = flag or self.traverse(root.right, targetSum - root.val, flag)
        if flag: return True
        return False


if __name__ == '__main__':
    # root=TreeNode(1,TreeNode(2,None,TreeNode(3)),TreeNode(4,TreeNode(5),TreeNode(6,TreeNode(7))))
    root = TreeNode(1, TreeNode(2))
    # root=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(3)),TreeNode(2,TreeNode(3),TreeNode(4)))
    # root=TreeNode()

    print(Solution().hasPathSum(root=root, targetSum=1))
