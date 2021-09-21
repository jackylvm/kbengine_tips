#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Created: 2021-09-05 15:46:54
# Author: Jacky (jackylvm@foxmail.com>)
# -----
# HISTORY:
# Date      			By			Comments
# --------------------	---------	-------------------
#
# -----------------------------------------------------

class EntityCall(object):
    """脚本层与实体远程交互的常规手段(其他参考:allClients、otherClients、clientEntity).

    EntityCall对象在C++底层实现非常简单,它只包含了实体的ID、目的地的地址、实体类型、EntityCall类型.
    当用户请求一次远程交互时,底层首先能够通过实体类型找到实体定义的描述,通过实体定义的描述对用户输入的数据进行检查,
    如果检查合法那么底层将数据打包并发往目的地,目的地进程根据协议进行解包最终调用到脚本层.

    注意: EntityCall只能调用其对应def文件中声明过的方法,不能访问实体的属性以及其他任何信息.

    一个实体最多可以包含三个部分:
        client:当实体包括客户端部分时(通常为玩家),在服务端可以访问实体的client(EntityCall)属性.
        base:当实体的一部分创建在Baseapp时,在非当前Baseapp中可以访问实体的base(EntityCall)属性.
        cell:当实体的一部分创建在Cellapp时,在非当前Cellapp中可以访问实体的cell(EntityCall)属性.

    举例:
        Avatar.def中定义client远程方法:
            <ClientMethods>
                <hello>
                </hello>
            </ClientMethods>
        client\Avatar.py
            class Avatar:
                def hello(self):
                    print("hello")

    在GUIConsole工具的Debug页输入框中输入(请先在左边列表中勾选要调试的进程):
    首先在服务端Baseapp的日志找到玩家实体(Avatar)的ID, 然后通过实体ID获得玩家实体(Avatar)或者EntityCall:
    >>> KBEngine.entities[玩家ID].client.hello()

    此时客户端log文件中将输出"hello", 一次远程调用过程完成.
    """


class BaseEntityCall(EntityCall):
    """"""


class CellEntityCall(EntityCall):
    """"""


class ClientEntityCall(EntityCall):
    """"""
