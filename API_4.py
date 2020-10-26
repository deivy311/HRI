from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import trafilatura
try: 
    from googlesearch import search 
  
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "head ache medicinenet.com"
res=search(query, tld="co.in", num=15, stop=15, pause=2)
buttoms={}
for j in res: 
    # with urllib.request.urlopen(j) as url:
    # url=Request(j, headers={'User-Agent': 'Mozilla/5.0'}) 
    # webpage=urlopen(url).read()
    # soup = BeautifulSoup(webpage, "html.parser")
    # print(soup)

    # print(j) 
    # body_res=soup.find('body')
    # print(body_res)
    downloaded = trafilatura.fetch_url(j)
    res=trafilatura.extract(downloaded, target_language='en')
    temp_buttoms=res[1]
    temp_buttoms.update(res[2])
    if (bool(temp_buttoms)):
        buttoms.update(temp_buttoms)
        print(j)
    if len(buttoms)>=4:
        print("got it!")
        break
    # if res
    

