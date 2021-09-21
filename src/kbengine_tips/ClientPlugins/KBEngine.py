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
# KBEngine模块提供了逻辑脚本层访问实体的部分, 以及当前space的数据等等.
import Math
import Types

# --------------KBEngine模块的成员属性--------------------------------
# 这是正运行在当前脚本环境的组件.(至今为止)可能值有'cell', 'base', 'client', 'database', 'bot' 和 'editor'.
# 这是一个只读变量,最好不要给他赋值
component = "client"

# entities是一个字典对象,包含当前进程上所有的实体.
# 说明:
#     entities是一个字典对象,包含当前进程上所有的实体.
#     调试泄露的实体(调用过destroy却没有释放内存的实体,通常是由于被引用导致无法释放):
#
#     >>> KBEngine.entities.garbages.items()
#     [(1025, Avatar object at 0x7f92431ceae8.)]
#     >>> e = _[0][1]
#     >>> import gc
#     >>> gc.get_referents(e)
#     [{'spacesIsOk': True, 'bootstrapIdx': 1}, ]
#
#     调试泄露的KBEngine封装的Python对象:
#     KBEngine.debugTracing
#     类型: Entities
entities = Types.Entities()

# 实体的uuid,改ID与实体本次登录绑定.当使用重登陆功能时服务端会与此ID进行比对,判断合法性.
entity_uuid = 0

# 当前客户端所控制的实体的ID.
entity_id = 0

# 当前客户端控制的实体所在的空间ID(也可以理解为所在对应的场景、房间、副本).
spaceID = 0


# ----------------KBEngine模块的成员函数--------------------------------------
def login(username, password):
    """登录账号到KBEngine服务端.

    注意:如果插件与UI层使用事件交互模式,在UI层不要直接调用,请触发一个"login"事件给插件,事件附带数据username和password.

    :param username:str,用户名.
    :param password:str,密码.

    :return:
    """
    pass


def createAccount(username, password):
    """请求向KBEngine服务端创建一个登录账号.

    注意:如果插件与UI层使用事件交互模式,在UI层不要直接调用,请触发一个"createAccount"事件给插件,事件附带数据username和password.

    :param username:str,用户名.
    :param password:str,密码.

    :return:
    """
    pass


def reloginBaseapp():
    """请求重登录到KBEngine服务端(通常在掉线之后希望更及时的连接到服务端并继续控制服务端角色时使用).

    注意:如果插件与UI层使用事件交互模式,在UI层不要直接调用,请触发一个"reloginBaseapp"事件给插件,事件附带数据为空.

    :return:
    """
    pass


def player():
    """获得当前客户端所控制的实体.

    :return:Entity,返回控制的实体,如果不存在(如:未能连接到服务端)则返回空.
    """
    pass


def resetPassword(username):
    """请求loginapp重置账号的密码,服务端将会向该账号绑定的邮箱发送一封重置密码邮件(通常是忘记密码功能使用).

    :param username:str,用户名.

    :return:
    """
    pass


def bindAccountEmail(emailaddress):
    """请求baseapp绑定账号的email地址.

    :param emailaddress:str,邮箱地址.

    :return:
    """
    pass


def newPassword(oldpassword, newpassword):
    """请求设置账号的新密码.

    :param oldpassword:str,旧密码.
    :param newpassword:str,新密码.

    :return:
    """
    pass


def findEntity(entityID):
    """通过实体的ID查找实体的实例对象.

    :param entityID:int32,实体ID.

    :return:Entity,存在返回实体实例,不存在返回空.
    """
    pass


def getSpaceData(key):
    """获取指定key的space数据.

    space数据由用户在服务端通过setSpaceData设置.

    :param key:str,一个字符串关键字.

    :return:str,指定key的字符串数据.
    """
    pass


class Entity:
    """类Entity的实例代表着在client上的游戏对象.

    一个Entity可以通过MAILBOX访问在base和cell应用程序上的等价的实体.这需要一组远程调用的函数(在实体的.def文件里指定).
    """

    # -------------KBEngine.Entity类的成员属性-------------------------------------------
    @property
    def direction(self):
        """这个属性描述的是Entity在世界空间中的朝向,用户可以改变这个属性,数据会同步到客户端.

        :return:Tuple,其中包含(roll, pitch, yaw),以弧度表示.
        """
        # 这样返回只是要告诉你他返回的是一个元组,具体内容要看具体实现
        return 0, 0, 0

    @property
    def id(self):
        """id是Entity的对象id.这个id是一个整型,在base,cell和client相关联的实体之间是相同的.

        只读属性

        :return: int32
        """
        return 0

    @property
    def position(self):
        """这个实体在世界空间中的坐标(x, y, z)

        这个属性可以被用户改变,改变后会同步到客户端.
        需要注意的是,不要引用这个属性,引用这个属性很有可能错误的修改了实体的真实坐标.

        例子:
            self.position.y = 10.0
        如果你想拷贝这个属性值可以使用如下方式:
            import Math
            self.copyPosition = Math.Vector3( self.position )

        :return:Vector3

            Vector3:
                描述和管理3D空間的向量.其中有x,y,z三个属性代表不同的轴向.

                例子:
                    import Math
                    v = Math.Vector3()
        """
        return Math.Vector3(0, 0, 0)

    @property
    def spaceID(self):
        """这个属性是实体所在的空间的ID,cell与客户端这个值都保持一致.

        :return: int
        """
        return 0

    @property
    def isOnGround(self):
        """如果这个属性的值为True,Entity在地面上,否则为False.

        只读属性

        :return: bool
        """
        return False

    @property
    def inWorld(self):
        """如果这个属性的值为True,Entity在世界内,否则为False.

        只读属性

        :return: bool
        """
        return False

    @property
    def className(self):
        """实体的类名

        :return:str
        """
        return self.__class__.__name__

    def baseCall(self, methodName, methodArgs):
        """调用该实体的base部分的方法.

        注意:实体在服务端必须有base部分,在客户端只有客户端控制的玩家实体才可以访问该方法.

        例子:
            js插件: entity.baseCall("reqCreateAvatar", roleType, name);
            c#插件: entity.baseCall("reqCreateAvatar", new object[]{roleType, name});

        :param methodName:str,方法名称.
        :param methodArgs:objects,方法参数列表.

        :return: 由于是远程调用,不可能阻塞等待返回,因此无返回值.
        """
        pass

    def cellCall(self, methodName, methodArgs):
        """调用该实体的cell部分的方法.

        注意:实体在服务端必须有cell部分,在客户端只有客户端控制的玩家实体才可以访问该方法.

        例子:
            js插件: entity.cellCall("xxx", roleType, name);
            c#插件: entity.cellCall("xxx", new object[]{roleType, name});

        :param methodName:str,方法名称.
        :param methodArgs:objects,方法参数列表.

        :return: 由于是远程调用,不可能阻塞等待返回,因此无返回值.
        """
        pass

    def onDestroy(self):
        """实体被销毁时调用.

        :return:
        """
        pass

    def onEnterWorld(self):
        """实体进入游戏世界后调用

        如果实体非客户端控制实体,则表明实体进入了服务端上客户端控制的实体的AOI范围,此时客户端可以看见这个实体了.
        如果实体是客户端控制的实体则表明该实体已经在服务端创建了cell并进入了space.

        :return:
        """
        pass

    def onLeaveWorld(self):
        """实体离开游戏世界后调用

        如果实体非客户端控制实体,则表明实体离开了服务端上客户端控制的实体的AOI范围,此时客户端看不见这个实体了.
        如果实体是客户端控制的实体则表明该实体已经在服务端销毁了cell并离开了space.

        :return:
        """
        pass

    def onEnterSpace(self):
        """客户端控制的实体进入了一个新的space.

        :return:
        """

    def onLeaveSpace(self):
        """客户端控制的实体离开了当前的space.

        :return:
        """
