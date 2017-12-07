import re
p=re.compile('a.b')
m=p.match("aab")
print(m)
m=p.match("a0b")
print(m)
m=p.match("abc")
print(m)
