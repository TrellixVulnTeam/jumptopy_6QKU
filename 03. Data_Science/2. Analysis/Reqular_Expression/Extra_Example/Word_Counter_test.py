import urllib.request, re
from collections import Counter

doc = """
양국 관계의 발전은 한국과 중국 국민이 보다 나은 삶을 살 수 있게 하였으며, 동북아가 대립과 갈등을 지양하고 협력과 평화의 길로 나아가게 하는 데에도 크게 기여했다고 평가합니다. 역사적으로도 그랬습니다. 중국이 번영하고 개방적이었을 때 한국도 함께 번영하며 개방적인 나라로 발전했습니다. 당나라와 한국의 통일신라, 송나라와 한국의 고려, 명나라와 한국의 조선 초기가 양국이 함께 찬란한 문화를 꽃피웠던 대표적인 시기입니다.
"""
print(doc.find('\\xec'))
words = re.findall(r"\w+", doc)

# 카운터를 만들고 답을 출력한다.
print(Counter(words).most_common(10))