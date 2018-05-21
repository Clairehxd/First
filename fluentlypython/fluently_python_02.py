# -*- coding:utf-8 -*-

from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):     #%r
        return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


c, d = Vector(1,2), Vector(3,4)
print('%r' % c)

'''
跟运算符无关的特殊方法：
字符串/字节序列表示形式：__repr__、__str__、__format__、__bytes__
数值转换：__abs__、__bool__、__complex__、__int__、__float__、__hash__、__index__
集合模拟：__len__、__getitem__、__setitem__、__delitem__、__contains__
迭代枚举：__iter__、__reversed__、__next__
可调用模拟：__call__
上下文管理：__enter__、__exit__
实例创建与销毁：__new__、__init__、__del__
属性管理：__getattr__、__getattribute__、__setattr__、__delattr__、__dir__
属性描述符：__get__、__set__、__delete__
跟类相关的服务：__prepare__、__instancecheck__、__subclasscheck__

跟运算符有关的特殊方法：
一元运算符：__neg__ -、__pos__ +、__abs__ abs()
众多比较运算符：__lt__ <、__le__ <=、__eg__ ==、__ne__ !=、__gt__ >、__ge__ >=
算术运算符：__add__ +、__sub__ -、__mul__ *、__truediv__ /、__floordiv__ //、
__mod__ %、__divmod__ divmod()、__pow__ **或pow()、__round__() round()
反向算术运算符：__radd__、__rsub__、__rmul__、__rtruediv__、__rfloordiv__、__rmod__、__rdivmod__
增量赋值算术运算符：__iadd__、__isub__、__imul__、__itruediv__、__imod__、__ipow__
位运算符：__invert__ ~、__lshift__ <<、__rshift__ >>、__and__ &、__or__ |、__xor__ ^
反向位运算符：__rlshift__、__rrshift__、__rand__、__rxor__、__ror__
增量赋值位运算符：__ilshift__、__irshift__、__iand__、__ixor__、__ior__

'''
