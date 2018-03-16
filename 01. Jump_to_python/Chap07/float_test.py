import  re

pat = re.compile(r'^[0-9]+$')
# pat = re.compile(r'^[0-9\.]+$')
p=re.compile(pat)
m=p.match("5.1")
print(m)