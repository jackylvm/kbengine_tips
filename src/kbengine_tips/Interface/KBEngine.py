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
# KBEngine模块主要处理KBEngine服务端与第三方平台的接入接出工作.

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


def accountLoginResponse(commitName, realAccountName, extraDatas, errorCode):
    """在onRequestAccountLogin被回调后,脚本需要调用此接口给出登陆处理结果.

    :param commitName:string,客户端请求时所提交的名称.
    :param realAccountName:string,返回真实的账号名称(没有特殊要求通常就是commitName,使用各种别名账号登陆时可用到).
    :param extraDatas:bytes,客户端请求时所附带的数据,可将数据转发第三方平台,在此提供对其进行修改的机会.
    :param errorCode:integer,错误码.如果需要中断用户的行为可在此设置错误码,
                    错误码可参考(KBEngine.SERVER_ERROR_*, 描述在kbengine/kbe/res/server/server_errors.xml),
                    否则提交KBEngine.SERVER_SUCCESS代表允许此处登陆.
   """


def createAccountResponse(commitName, realAccountName, extraDatas, errorCode):
    """在onRequestCreateAccount被回调后,脚本需要调用此接口给出账号创建处理结果.

    :param commitName:string,客户端请求时所提交的名称.
    :param realAccountName:string,返回真实的账号名称(没有特殊要求通常就是commitName,使用各种别名账号登陆时可用到).
    :param extraDatas:bytes,客户端请求时所附带的数据,可将数据转发第三方平台,在此提供对其进行修改的机会.
    :param errorCode:integer,错误码.如果需要中断用户的行为可在此设置错误码,
                    错误码可参考(KBEngine.SERVER_ERROR_*, 描述在kbengine/kbe/res/server/server_errors.xml),
                    否则提交KBEngine.SERVER_SUCCESS代表允许此处登陆.
    """


def chargeResponse(orderID, extraDatas, errorCode):
    """在onRequestCharge被回调后,脚本需要调用此接口给出计费处理结果.

    :param orderID:uint64,订单的ID.
    :param extraDatas:bytes,客户端请求时所附带的数据,可将数据转发第三方平台,在此提供对其进行修改的机会.
    :param errorCode:integer,错误码.如果需要中断用户的行为可在此设置错误码,
                    错误码可参考(KBEngine.SERVER_ERROR_*, 描述在kbengine/kbe/res/server/server_errors.xml),
                    否则提交KBEngine.SERVER_SUCCESS代表允许此处登陆.
    """


def delTimer(id):
    """函数delTimer用于移除一个注册的定时器,移除后的定时器不再执行.

    只执行1次的定时器在执行回调后自动移除,不必要使用delTimer移除.如果delTimer函数使用一个无效的id(例如已经移除),将会产生错误.
    到KBEngine.addTimer参考定时器的一个使用例子.

    :param id:integer,它指定要移除的定时器id.
    """


def onInterfaceAppReady():
    """当前进程已经准备好的时候回调此函数.

    注意:该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中.
    """


def onInterfaceAppShutDown():
    """进程关闭会回调此函数.

    注意:该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中.
    """


def onRequestCreateAccount(registerName, password, datas):
    """当客户端请求服务器创建账号时,该回调被调用.

    可在此函数内数据进行检查和修改,将最终结果通过KBEngine.createAccountResponse提交给引擎.
    注意:该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中.

    :param registerName:string,客户端请求时所提交的名称.
    :param password:string,密码.
    :param datas:bytes,客户端请求时所附带的数据,可将数据转发第三方平台.
    """


def onRequestAccountLogin(loginName, password, datas):
    """当客户端请求服务器登陆账号时,该回调被调用.

    可在此函数内数据进行检查和修改,将最终结果通过KBEngine.accountLoginResponse提交给引擎.
    注意:该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中.

    :param loginName:loginName string,客户端请求时所提交的名称.
    :param password:string,密码.
    :param datas:bytes,客户端请求时所附带的数据,可将数据转发第三方平台.
    """


def onRequestCharge(ordersID, entityDBID, datas):
    """当请求计费时(通常是baseapp上调用了KBEngine.charge),该回调被调用.

    可在此函数内数据进行检查和修改,将最终结果通过KBEngine.chargeResponse提交给引擎.
    注意:该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中.

    :param ordersID:uint64,订单的ID.
    :param entityDBID:uint64,提交订单的实体DBID.
    :param datas:bytes,客户端请求时所附带的数据,可将数据转发第三方平台.
    """
