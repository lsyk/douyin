import urllib.request
import re
import json
import sys
url = input("请输入：")

#url = 'http://v.douyin.com/hQteJ8/'
headers = {
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
#print(response.read().decode('utf-8'))
html =  response.read().decode('utf-8')                                   
#print(re.findall(r"itemId: \"([0-9]+)\"|dytk: \"(.*)\"",html))
itemId = re.findall(r"itemId: \"([0-9]+)\"",html)[0]
dytk = re.findall(r"dytk: \"(.*)\"",html)[0]
#print(itemId)
#print(dytk)
url = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids="+itemId+"&dytk="+dytk
#print(url)
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
#print(response.read().decode('utf-8'))
data = json.loads(response.read().decode('utf-8'))
print(data['item_list'][0]['video']['play_addr']['url_list'][0])

url = data['item_list'][0]['video']['play_addr']['url_list'][0]
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
print(response.geturl())
