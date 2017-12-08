import re
str='''a
b'''
# str='a\nb'
# p = re.compile('a.b',re.DOTALL)
p = re.compile('a.b',re.S)
m = p.match(str)
print(m)