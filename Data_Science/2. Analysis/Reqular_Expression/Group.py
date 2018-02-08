import re
#A+
p = re.compile('(ABC)+')
m = p.search("ABCABC")

print(m)