import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser

url = 'https://www.virustotal.com/vtapi/v2/file/scan'
params = {'apikey': '37b5d1312dcee2d2b31f198233162d098248bb35eed2b4b3cf40aae673ba2344'}
files = {'file': ('myfile.exe', open('myfile.exe', 'rb'))}
response = requests.post(url, files=files, params=params)
res=response.json()
linkvs=res['permalink']
webbrowser.open_new(str(linkvs))

# bs = BeautifulSoup(html, 'lxml')
# print(bs)
# for l in  bs.findAll('td'):
#     if l.find('Detection ratio:'):
#         l.find('Detection ratio:').extract()
#     print(l.getText())
