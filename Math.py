#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Created: 2021-08-29 21:23:54
# Author: Jacky (jackylvm@foxmail.com>)
# -----
# HISTORY:
# Date      			By			Comments
# --------------------	---------	-------------------
#
# -----------------------------------------------------

class Vector2():
    """描述和管理2D空间的向量.

    其中有x,y两个属性代表不同的轴向.
    """

    def __init__(self, x, y):
        """"""
        self._x = x
        self._y = y

    @property
    def x(self):
        """"""
        return self._x

    @x.setter
    def x(self, x):
        """"""
        self._x = x

    @property
    def y(self):
        """"""
        return self._y

    @y.setter
    def y(self, y):
        """"""
        self._y = y


class Vector3():
    """描述和管理3D空间的向量.

    其中有x,y,z三个属性代表不同的轴向.
    """

    def __init__(self, x, y, z):
        """"""
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        """"""
        return self._x

    @x.setter
    def x(self, x):
        """"""
        self._x = x

    @property
    def y(self):
        """"""
        return self._y

    @y.setter
    def y(self, y):
        """"""
        self._y = y

    @property
    def z(self):
        """"""
        return self._z

    @z.setter
    def z(self, z):
        """"""
        self._z = z


class Vector4():
    """描述和管理4D空间的向量.

    其中有a,x,y,z三个属性代表不同的轴向.
    """

    def __init__(self, a, x, y, z):
        """"""
        self._a = a
        self._x = x
        self._y = y
        self._z = z

    @property
    def a(self):
        """"""
        return self._a

    @a.setter
    def a(self, a):
        """"""
        self._a = a

    @property
    def x(self):
        """"""
        return self._x

    @x.setter
    def x(self, x):
        """"""
        self._x = x

    @property
    def y(self):
        """"""
        return self._y

    @y.setter
    def y(self, y):
        """"""
        self._y = y

    @property
    def z(self):
        """"""
        return self._z

    @z.setter
    def z(self, z):
        """"""
        self._z = z
