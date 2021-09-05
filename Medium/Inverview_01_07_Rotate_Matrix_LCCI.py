#!/usr/bin/env python3

from typing import List


class Solution(object):
    # Inverview 01.07. Rotate Matrix LCCI
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Did not figure out
        for i in range(len(matrix) - 1):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][-1 - j] = matrix[i][-1 - j], matrix[i][j]
        # print(matrix)

        ##################################################
        # WRONG SOLUTION #################################
        ##################################################
        # matrix_rot=[]
        # row_temp=[]
        # for row in range(len(matrix)):
        #     for col in range(len(matrix)):
        #         row_temp.extend([matrix[-1-col][row]])
        #     matrix_rot.append(row_temp)
        #     row_temp=[]
        # return matrix_rot
        ##################################################


if __name__ == '__main__':
    Solution().rotate(matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])   # no return
