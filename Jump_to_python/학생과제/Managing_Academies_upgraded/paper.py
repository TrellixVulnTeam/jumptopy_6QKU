# import os
#
# print("goto가 되나?")
# print(os.getcwd())
# os.chdir("..\\..")
# print(os.getcwd())

#
# a = { 1 : 'a', 2 : 'b'}
# b = { 3 : 'c', 4 : 'd'}
#
# print(a)
# print(b)
#
# a = b
#
# print(a)
#
# class a() :
#     def __init__(self, a, b) :
#         self.a = a
#         self.b = b
#
# def make_class() :
#     cc = a(2, 3)
#     return cc
#
# def print_returned_class(instance) :
#     print(instance.a)
#     print(instance.b)
#
# print_returned_class(make_class())

import re

p = re.compile("asd")
a = "asdfef"
b = "aaaa"

d = p.match(a)
print(p.match(a))
print(p.match(b))

if b == None : print("없다")
if d != None : print(d.group())

