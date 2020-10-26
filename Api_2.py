#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

try: 
    from googlesearch import search 
  
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "head ache medicinenet.com"
res=search(query, tld="co.in", num=10, stop=10, pause=2)
for j in res: 
    # with urllib.request.urlopen(j) as url:
    url=Request(j, headers={'User-Agent': 'Mozilla/5.0'}) 
    webpage=urlopen(url).read()
    soup = BeautifulSoup(webpage, "html.parser")
    print(soup)

    print(j) 
    body_res=soup.find('body')
    print(body_res)