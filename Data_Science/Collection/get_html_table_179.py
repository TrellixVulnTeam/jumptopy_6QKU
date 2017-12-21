import urllib.request
from bs4 import BeautifulSoup

max_page = 10
result = []
for page_idx in range(max_page):
    Cheogajip_URL = 'http://www.cheogajip.co.kr/establish02_02.html?page=%s&search=&keyword='%str(page_idx+1)
    print(Cheogajip_URL)

    response = urllib.request.urlopen(Cheogajip_URL)
    soupData = BeautifulSoup(response.read().decode('CP949'),'html.parser')

    store_trs = soupData.find_all('tr',attrs={'align':'center','bgcolor':'#FFFFFF'})
    print("End")
    if (store_trs):
        for store_tr in store_trs:
            tr_tag = list(store_tr.strings)

            chain_name = tr_tag[1]
            address = tr_tag[3]
            phone_number = tr_tag[5]
            result.append(chain_name+','+address+','+phone_number)

print("end")