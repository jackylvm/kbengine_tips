#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Created: 2021-08-29 19:22:08
# Author: Jacky (jackylvm@foxmail.com>)
# -----
# HISTORY:
# Date      			By			Comments
# --------------------	---------	-------------------
#
# -----------------------------------------------------
# KBEngine模块提供了Python脚本控制对特定类型的日志进行分析和转储等能力.

# ----------------KBEngine模块的成员函数--------------------------------------
def addTimer(initialOffset, repeatOffset=0, callbackObj=None):
    """注册一个定时器,定时器由回调函数callbackObj触发,回调函数将在"initialOffset"秒后被执行第1次,而后将每间隔"repeatOffset"秒执行1次.

    例子:
        # 这里是使用addTimer的一个例子
        import KBEngine

        # 增加一个定时器,5秒后执行第1次,而后每1秒执行1次,用户参数是9
        KBEngine.addTimer( 5, 1, onTimer_Callbackfun )

        # 增加一个定时器,1秒后执行,用户参数缺省是0
        KBEngine.addTimer( 1, onTimer_Callbackfun )

        def onTimer_Callbackfun( id ):
            print "onTimer_Callbackfun called: id %i" % ( id )
            # if 这是不断重复的定时器,当不再需要该定时器的时候,调用下面函数移除:
            #     KBEngine.delTimer( id )

    :param initialOffset:float,指定定时器从注册到第一次回调的时间间隔(秒).
    :param repeatOffset:float,指定第一次回调执行后每次执行的时间间隔(秒).必须用函数delTimer移除定时器,否则它会一直重复下去.值小于等于0将被忽略.
    :param callbackObj:function,指定的回调函数对象.

    :return:integer,该函数返回timer的内部id,这个id可用于delTimer移除定时器.
    """


def delTimer(id):
    """函数delTimer用于移除一个注册的定时器,移除后的定时器不再执行.

    只执行1次的定时器在执行回调后自动移除,不必要使用delTimer移除.如果delTimer函数使用一个无效的id(例如已经移除),将会产生错误.
    到KBEngine.addTimer参考定时器的一个使用例子.

    :param id:integer,它指定要移除的定时器id.
    """


def onLoggerAppReady():
    """当前进程已经准备好的时候回调此函数.

    注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中.
    """


def onLoggerAppShutDown():
    """进程关闭会回调此函数.

    注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中.
    """


def onLogWrote(datas):
    """如果这个函数在脚本中有实现,logger进程获得了一条新日志,该回调函数被调用.

    数据库接口在kbengine_defs.xml->dbmgr->databaseInterfaces定义.
    注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中.

    :param datas: bytes,日志数据.
    """


def onReadyForShutDown():
    """如果这个函数在脚本中有实现,当进程准备退出时,该回调函数被调用.

    可以在收到回调时进行脚本层的数据清理工作,以保证程序的安全退出.
    注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中.

    :return:bool,如果返回True,则允许进入进程退出流程,返回其它值则进程会过一段时间后再次询问.
    """
