#!/usr/bin/env python3


class Solution(object):
    # 151. Reverse Words in a String
    def reverseWords(self, s: str) -> str:
        reversed_words = ''
        word_ind = []
        if s[0] != 0 and s[0] != ' ':
            start = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1] and s[i - 1] == ' ':
                start = i
            elif s[i] != s[i - 1] and s[i] == ' ':
                end = i
                word_ind.append([start, end])
            elif i == len(s) - 2 and s[i] != ' ':
                end = i
                word_ind.append([start, end])
        if i == len(s) - 1 and s[i] != ' ':
            end = i
            word_ind.append([start, end])
        for i in range(len(word_ind) - 1, -1, -1):
            reversed_words += s[word_ind[i][0]:word_ind[i][1]] + ' '

        return reversed_words[:-1:]

    def reverseWords_attemp2(self, s: str) -> str:
        reversed_words = ''
        if s[-1] != 0 and s[-1] != ' ':
            end = len(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] != s[i - 1] and s[i] == ' ':
                end = i
            elif s[i] != s[i - 1] and s[i - 1] == ' ':
                start = i
                reversed_words += ' ' + s[start:end]
        if i == 0 and end > 0 and s[i - 1] != ' ':
            start = 0
            reversed_words += ' ' + s[start:end]
        return reversed_words[1::]


if __name__ == '__main__':
    print(Solution().reverseWords(s=" a good   example  "))
    print(Solution().reverseWords_attemp2(s="   fffff ff gg ee"))
