# KBEngine_tips

---
* [介绍](#--0x01-介绍)
* [安装](#--0x02-安装)
* [使用](#--0x03-使用)

## - 0x01 介绍

[KEBengine](https://github.com/kbengine/kbengine.git) 是一款开源的MMOG游戏服务端引擎,在编辑游戏逻辑时需要使用KEBengine提供的函数.
由于编辑器不能检索到KEBengine提供的函数,导致没有自动提示.该项目提供KEBengine的相关函数,提供提示能力.

## - 0x02 安装

```shell
pip install kbengine_tips
```

## - 0x03 使用

在需要导入KBEngine的地方,加入如下代码
```python
try:
    import KBEngine
except ImportError:
    # 这里这样做就是为了编码方便
    # 实际代码运行的时候是不会走到这里的
    from kbengine_tips.BaseApp import KBEngine
```
在编辑代码是,因为import KBEngine会报错,所以会使用下面的from kbengine_tips.BaseApp import KBEngine代码.