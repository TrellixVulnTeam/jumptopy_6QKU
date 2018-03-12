import re
re_str='a.b'
p=re.compile(re_str)
m=p.match("aab")
print(m)
print(m.group())
m=p.match("a0b")
print(m)
m=p.match("abc")
print(m)

re_str='a[.]b'
p=re.compile(re_str)
m=p.match("a.b")
print(m)
print(m.group())
