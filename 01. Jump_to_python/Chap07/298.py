import re
re_str='a[abc]'
p=re.compile(re_str)
m=p.match("aab")
print(m)
m=p.match("a")
print(m)
m=p.match("before")
print(m)
m=p.match("dude")
print(m)
