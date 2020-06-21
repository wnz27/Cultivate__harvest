# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/3/29 23:01
__author__ = '27'


class Vector:
    def __init__(self, lst):
        # 防止引用在外部被修改，所以复制一份
        self._values = list(lst)

    def __add__(self, other):
        """
        向量加法，返回结果向量
        :param other: 另一个Vector实例对象
        :return: 结果向量实例
        """
        assert len(self) == len(other), "Error in adding. Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        """
        向量减法，返回结果向量
        :param other: 另一个Vector实例对象
        :return: 结果向量实例
        """
        assert len(self) == len(other), "Error in adding. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, other)])

    def __iter__(self):
        """
        防止直接使用_values，被for之类调用的时候直接使用实例即可，不用显式访问私有变量。
        :return: 向量的迭代器
        """
        return self._values.__iter__()

    def __len__(self):
        """返回向量长度（有多少个元素），即向量维度"""
        return len(self._values)

    def __getitem__(self, index):
        """取向量的第index个元素"""
        return self._values[index]

    # 系统调用
    def __repr__(self):
        return "Vector({})".format(self._values)

    # 使用者调用
    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
