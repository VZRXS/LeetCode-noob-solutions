#!/usr/bin/env python3

from typing import List


class Solution(object):
    # Inverview 01.08. Zero Matrix LCCI
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ind = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    ind.append([i, j])
        if len(ind) > 0:
            for i in range(len(ind)):
                matrix[ind[i][0]][:] = [0 for _ in range(len(matrix[0]))]
                for j in range(len(matrix)):
                    matrix[j][ind[i][1]] = 0
        print(matrix)


if __name__ == '__main__':
    print(Solution().setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
