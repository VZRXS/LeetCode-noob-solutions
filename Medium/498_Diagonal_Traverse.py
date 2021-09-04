#!/usr/bin/env python3

from typing import List


class Solution(object):
    # 498. Diagonal Traverse
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        if len(mat) == 1 or len(mat[0]) == 1:
            return [x for y in mat for x in y]

        diag = []
        diag_temp = []
        h = len(mat)
        w = len(mat[0])
        num = 0

        for i in range(min(h, w) - 1):
            for j in range(i + 1):
                diag_temp.append([i - j, j])
            diag.extend(diag_temp[::(-1)**num])
            diag_temp = []
            num += 1
        if w >= h:
            for i in range(w - h + 1):
                for j in range(h):
                    diag_temp.append([h - j - 1, j + i])
                diag.extend(diag_temp[::(-1)**num])
                diag_temp = []
                num += 1
            for i in range(h - 1):
                for j in range(h - i - 1):
                    diag_temp.append([h - j - 1, w - h + 1 + j + i])
                diag.extend(diag_temp[::(-1)**num])
                diag_temp = []
                num += 1
        else:
            for i in range(h - w + 1):
                for j in range(w):
                    diag_temp.append([w - j + i - 1, j])
                diag.extend(diag_temp[::(-1)**num])
                diag_temp = []
                num += 1

            for i in range(w - 1):
                for j in range(w - i - 1):
                    diag_temp.append([h - j - 1, j + i + 1])
                diag.extend(diag_temp[::(-1)**num])
                diag_temp = []
                num += 1

        output = []
        for i in range(len(diag)):
            output.append(mat[diag[i][0]][diag[i][1]])

        return output


if __name__ == '__main__':
    print(Solution().findDiagonalOrder(
        mat=[[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]))
