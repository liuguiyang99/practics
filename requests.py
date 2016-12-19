import requests
conn = requests.session()
resp = conn.get('https://www.baidu.com/s?wd=findspace')

print(resp.request.headers)

#{'Connection': 'keep-alive', 'User-Agent': 'python-requests/2.4.3 CPython/3.4.2 Linux/3.16.0-4-amd64', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate'}

resp = conn.get('https://www.baidu.com/s?wd=findspace')
print(resp.request.headers)
#{'Connection': 'keep-alive', 'User-Agent': 'python-requests/2.4.3 CPython/3.4.2 Linux/3.16.0-4-amd64', 'Accept': '*/*', 'Cookie': 'BD_NOT_HTTPS=1; BDSVRTM=3; PSTM=1458389621; BIDUPSID=9CB03BE7D7F436EC2EE23C6E6EBE8EBD', 'Accept-Encoding': 'gzip, deflate'}