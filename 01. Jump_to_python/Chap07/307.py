import re
str='python'
# p = re.compile('[a-z]+')
# m = p.match(str)
m = re.match('[a-z]+',str)
print(m.group())
print(m.start())
print(m.end())
print(m.span())

str='3 python'
p = re.compile('[a-z]+')
m = p.search(str)
print(m.group())
print(m.start())
print(m.end())
print(m.span())
