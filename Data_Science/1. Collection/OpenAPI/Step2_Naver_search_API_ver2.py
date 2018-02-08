domain_list=[
    'www.chosun.com',
    'www.hani.com',
    'www.chosun.com',
    'www.joonang.com',
    'www.chosun.com',
    'www.hani.com',
    'www.chosun.com',
    'www.chosun.com',
]

domain_analysis=[{}]

def add_domain(domain):
    is_found = False
    for element in domain_analysis:
        if domain in element.keys():
            element[domain] = element[domain]+1
            is_found = True

    if is_found == False:
        domain_analysis.append({domain,1})

for domain in domain_list:
    add_domain(domain)

# sorted_list = sorted(domain_analysis,reverse=True)
# print(sorted_list)


