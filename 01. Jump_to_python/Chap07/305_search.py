import re
str='python'
p = re.compile('[a-z]+')
print(p.match(str))
print(p.search(str))

str='3 python'
print(p.match(str))
print(p.search(str))

str='life is too short'
print(p.findall(str))

result = p.finditer(str)
for r in result:
    print(r.group())