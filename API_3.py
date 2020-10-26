from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import trafilatura
import xml.etree.ElementTree as ET
# downloaded = trafilatura.fetch_url('https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/')
downloaded = trafilatura.fetch_url('https://www.medicinenet.com/headache/article.htm')
# downloaded = trafilatura.fetch_url('https://www.medicinenet.com/migraine/article.htm')
# downloaded = trafilatura.fetch_url('https://www.nhs.uk/conditions/headaches/')
res=trafilatura.extract(downloaded, target_language='en')
res2=trafilatura.extract(downloaded, xml_output=True, include_comments=True, target_language='en')
res2_1=trafilatura.extract(downloaded, json_output=True, include_comments=True, target_language='en')

print(soup)
# res3=xmltotxt_D(res2)
# # res3=trafilatura.core.bare_extraction(downloaded)
# # res4=trafilatura.core.bare_extraction(downloaded, xml_output=True, include_comments=False)
# print(res3)
