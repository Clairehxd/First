# -*- coding:utf-8 -*-

#chapter02

#列表推导
x = 'ABC'
y = [ord(x) for x in x if ord(x) > 65]
print('01')
print(x, y)
z = list(filter(lambda c: c > 65, map(ord, x)))
print(x, z)

#生成器表达式
symbols = 'ABCDEF'
print('02')
print(tuple(ord(symbol) for symbol in symbols))
import array
print(array.array('I', (ord(symbol) for symbol in symbols)))




