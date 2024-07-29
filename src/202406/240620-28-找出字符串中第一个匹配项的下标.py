"""
日期: 2024年6月21日
题目: 28.找出字符串中第一个匹配项的下标
地址: https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""


def str_str(haystack: str, needle: str) -> int:
    """
    第一种方法是利用Python切片功能实现的, 从每个字符开始取等同于子串长度的切片, 然后与子串的内容进行比对.
    :param haystack:
    :param needle:
    :return:
    """
    length = len(needle)
    for i in range(len(haystack) - length + 1):
        if haystack[i:i + length] == needle:
            return i
    return -1


def str_str_2(haystack: str, needle: str) -> int:
    """
    第二种方法采用类似于KMP算法的思路解决, 相对于第一种方法, 这种方法的泛用性更强.
    :param haystack:
    :param needle:
    :return:
    """
    m, n = len(haystack), len(needle)  # 首先获取两个字符串的长度
    char_list1, char_list2 = list(haystack), list(needle)

    for i in range(m - n):
        a, b = i, 0
        while (b < n) and (char_list1[a] == char_list2[b]):
            a += 1
            b += 1
        if b == n:
            return i

    return -1
