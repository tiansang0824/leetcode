"""
2024年6月19日
题目：1768-交替合并字符串
https://leetcode.cn/problems/merge-strings-alternately/
"""


def merge_alternately(word1: str, word2: str) -> str:
    l1, l2 = len(word1), len(word2)
    i, j = 0, 0

    new_str = ""

    while i < len(word1) and j < len(word2):
        if i <= j:
            new_str = new_str + word1[i]
            i += 1
        else:
            new_str = new_str + word2[j]
            j += 1

    if l1 == l2:
        new_str = new_str + word2[j]
    elif l1 > l2:
        new_str = new_str + word1[i:]  # 或者也可以写成 new_str = new_str + word1[i:]
    else:
        new_str = new_str + word2[j:]  # 或者也可以写成 new_str = new_str + word2[j:]

    return new_str


def super_solu(word1: str, word2: str):
    """
    第二种解法
    :param word1:
    :param word2:
    :return:
    """
    arr = ''
    m, n = len(word1), len(word2)
    i = 0
    while i < m:
        arr = arr + word1[i]
        if i < n:
            arr = arr + word2[i]
        i += 1

    if n > m:
        arr += word2[i:n]
    return arr


if __name__ == '__main__':
    print(merge_alternately("abc", "pqr"))
    print(super_solu("abc", "pqr"))
