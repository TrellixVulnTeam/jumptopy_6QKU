import re
# p = re.compile(r'\bclass\b')
#p = re.compile('\sclass\s')
p = re.compile('\bclass\b') # <-- 실행 되지 않음
# p = re.compile(' class ')
print(p.search('no class at all'))