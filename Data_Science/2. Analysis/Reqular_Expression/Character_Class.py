import re
p = re.compile(r"(\b\w+)\s+\1")
m = p.search("Paris in the the spring").group()
# m = p.search("Life is too short")


print(m)


