import re
import requests
from bs4 import BeautifulSoup


with open('restaurants_details',r) as read_f:
    while True:
        line = read_f.readline()
        if line:
            print line
        else:
            break


# base_url = 'https://restaurant.michelin.fr/restaurants/france/page-'
# for i in range(1, 340):
#     if i ==1:
#         url = 'https://restaurant.michelin.fr/restaurants/france'
#     else:
#         url = base_url+str(i)
#     print "进度：" + str(i) +"/339"
#
#     page = requests.get(url).text
#     pagesoup=BeautifulSoup(page, 'lxml')
#     all_href = pagesoup.find_all('a', {"class":"poi-card-link"})
#     for i in all_href:
#         pattern = 'href=\"(.*)\"'
#         result = re.findall(pattern, str(i))
#         with open("restaurants_details", "a") as f:
#             f.write("https://restaurant.michelin.fr"+result[0])
#             f.write("\n")
#             print "https://restaurant.michelin.fr"+result[0]