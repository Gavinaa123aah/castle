import re
import requests
from bs4 import BeautifulSoup
import json
urls_list = []
base_url = 'https://restaurant.michelin.fr/restaurants/france/page-'
for i in range(1, 10):
    if i ==1:
        url = 'https://restaurant.michelin.fr/restaurants/france'
    else:
        url = base_url+str(i)
    print "rate" + str(i) +"/339"

    page = requests.get(url).text
    pagesoup=BeautifulSoup(page, 'lxml')
    all_href = pagesoup.find_all('img', {"width":380})
    # print all_href
    for i in all_href:
        pattern = 'data-src=\"(.*?)\"\\sheight'
        result = re.findall(pattern, str(i))
        if len(result)!=0:
            urls_list.append({"url":result[0]})
            print result[0]
    with open ("img_urls.json","w") as f_url:
        json.dump(urls_list, f_url)


        # with open("restaurants_details", "a") as f:
        #     f.write("https://restaurant.michelin.fr"+result[0])
        #     f.write("\n")
        #     print "https://restaurant.michelin.fr"+result[0]