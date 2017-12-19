from bs4 import BeautifulSoup
html='<td class="title"><div class="tit3"><a href="/movie/bi/mi/basic.nhn?code=136872"title="미녀와 야수">미녀와 야수</a></div></td>'
soup=BeautifulSoup(html,'html.parser')
print(soup)
tag=soup.td
print(tag)
tag=soup.div
print(tag)
tag=soup.a
print(tag)
print(tag.name)