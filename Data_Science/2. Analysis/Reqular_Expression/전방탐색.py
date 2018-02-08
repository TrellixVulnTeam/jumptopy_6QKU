import re
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

p = re.compile(".+(?=:)") #':'는 소모되지 않는다.
m = p.search("http://google.com")
print(m.group())
