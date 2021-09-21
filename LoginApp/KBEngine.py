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

    :return:
    """


def onLoginAppReady():
    """当前进程已经准备好的时候回调此函数.

    注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中.

    :return:
    """


def onLoginAppShutDown():
    """进程关闭会回调此函数.

    注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中.

    :return:
    """


def onReuqestLogin(loginName, password, clientType, datas):
    """客户端请求服务器登陆账号时回调.

    此处可以对用户登陆做一些管理控制,
    例如：
        利用该接口可以在此截断用户的登陆,将请求记录下来进行排队并返回一个错误码告诉客户端排队状态,客户端通过不断登陆从此处获得状态.
    注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中.

    :param loginName:string,登陆时提交的账号名称.
    :param password:string,MD5密码.
    :param clientType:integer,客户端类型,客户端登陆时给出.
    :param datas:bytes,客户端请求时所附带的数据,可将数据转发第三方平台.

    :return:Tuple,返回值分别为(错误码,真实账号名,密码,客户端类别,客户端提交的数据datas),
            如果没有任何需要扩展修改的则通常返回值为毁掉传入的值(KBEngine.SERVER_SUCCESS, loginName, password, clientType, datas).
    """


def onLoginCallbackFromDB(loginName, accountName, errorno, datas):
    """客户端请求服务器登陆账号后由dbmgr返回的回调.

    注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中.

    :param loginName:string,登陆时提交的账号名称.
    :param accountName:string,真实的账号名称(由dbmgr处查询获得).
    :param errorno:integer,错误码,如果非KBEngine.SERVER_SUCCESS则表示登陆失败.
    :param datas:bytes,可能是任何数据,例如：第三方平台返回的数据或者由dbmgr以及interfaces中处理登陆时返回的数据.

    :return:
    """


def onRequestCreateAccount(accountName, password, data):
    """客户端请求服务器创建账号时回调.

    注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中.

    :param accountName:string,客户端提交的账号名称.
    :param password:string,MD5密码.
    :param data:bytes,客户端请求时所附带的数据,可将数据转发第三方平台.

    :return: Tuple,返回值分别为(错误码,真实账号名,密码,客户端提交的数据datas),
            如果没有任何需要扩展修改的则通常返回值为毁掉传入的值(KBEngine.SERVER_SUCCESS, loginName, password, datas).
    """


def onCreateAccountCallbackFromDB(accountName, errorno, datas):
    """客户端请求服务器创建账号后由dbmgr返回的回调.

    注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中.

    :param accountName: string,客户端提交的账号名称.
    :param errorno: integer,错误码,如果非KBEngine.SERVER_SUCCESS则表示登陆失败.
    :param datas: bytes,可能是任何数据,例如：第三方平台返回的数据或者由dbmgr以及interfaces中处理登陆时返回的数据.

    :return:
    """
