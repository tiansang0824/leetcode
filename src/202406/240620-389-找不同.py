"""
日期: 2024年6月20日
题目: 389-找不同
地址: https://leetcode.cn/problems/find-the-difference/
"""
from collections import Counter

"""
在这道题中,学到了:

1. 一个新的函数`zip`, 

该函数用于将传入的可迭代对象包装成一个列表, 他会将传入的可迭代对象全部转换为元组, 然后依次添加到一个列表中, 
传入的内容将会以元组的形式保存在列表中.

2. 以及对比不同列表容器/可迭代容器的方法:

先排序, 后对比.

"""


def find_difference(s: str, t: str) -> str:
    new_s = sorted(s) + [" "]
    new_t = sorted(t)

    for i, j in zip(new_s, new_t):
        if i != j:
            return j


def find_difference2(s: str, t: str) -> str:
    return (Counter(t) - Counter(s)).popitem()[0]


if __name__ == '__main__':
    str_s = "hello"
    str_t = "leahol"
    diff = find_difference(str_s, str_t)
    print(f"不同字符是: {diff}")
    diff2 = find_difference2(str_s, str_t)
    print(f"不同字符是: {diff}")
