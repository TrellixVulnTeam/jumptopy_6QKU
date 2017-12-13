import re
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())
p = re.compile("\+\w :")
m = p.search("+d :dfsf")
print(m.group())
m = p.search("d :dfsf")
print(m.group())
