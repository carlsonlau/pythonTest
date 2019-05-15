import requests
r = requests.get('http://sports.sina.com.cn/nba/')
print(r.status_code)
print(r.text)
print(r.content)
print(r.encoding)
print(r.apparent_encoding)