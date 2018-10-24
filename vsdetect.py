import requests
url = 'https://www.virustotal.com/vtapi/v2/file/scan'
params = {'apikey': '37b5d1312dcee2d2b31f198233162d098248bb35eed2b4b3cf40aae673ba2344'}
files = {'file': ('myfile.exe', open('myfile.exe', 'rb'))}
response = requests.post(url, files=files, params=params)
print(response.json())
