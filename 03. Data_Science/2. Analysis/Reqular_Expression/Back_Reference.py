import re

# p = re.compile(r"(\w+)\s")
# p = re.compile(r"\w+\s\w+")
# p = re.compile(r"(\w+)\s(\w+)")
p = re.compile(r"(\w+)\s\1")
m = p.search("sdf Hello Hello ")
print(m)

p = re.compile(r"(\w+)\s(\w+)\s\1\s\2")
m = p.search("sdf Hello World Hello World dkfjkdsfj ")
print(m)

p = re.compile(r"(\w+)\s(\w+)\s\2\s\1")
m = p.search("sdf Hello World Hello World World Hello dkfjkdsfj ")
print(m)
