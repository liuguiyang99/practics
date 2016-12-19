import gzip
import re  
import http.cookiejar  
import urllib.request  
import urllib.parse

def ungzip(data):  
    try:        # ���Խ�ѹ  
        print('���ڽ�ѹ.....')  
        data = gzip.decompress(data)  
        print('��ѹ���!')  
    except:  
        print('δ��ѹ��, �����ѹ')  
    return data
    
    
#��ȡ_xsrf   
def getXSRF(data):  
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)  
    strlist = cer.findall(data)  
    return strlist[0]  
#�����ļ�ͷ  
def getOpener(head):  
    #����һ��cookie��������������ӷ���������cookie�����أ������ڷ�������ʱ���ϱ��ص�cookie  
    cj = http.cookiejar.CookieJar()  
    pro = urllib.request.HTTPCookieProcessor(cj)  
    opener = urllib.request.build_opener(pro)  
    header = []  
    for key, value in head.items():  
        elem = (key, value)  
        header.append(elem)  
    opener.addheaders = header  
    return opener  
#����header��һ��header����Ҫ����һ������������Ǵ�ץ���İ�������ó��ġ�     
header = {  
    'Connection': 'Keep-Alive',  
    'Accept': 'text/html, application/xhtml+xml, */*',  
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',  
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',  
    'Accept-Encoding': 'gzip, deflate',  
    'Host': 'www.zhihu.com',  
    'DNT': '1'  
}  
   
url = 'http://www.zhihu.com/'  
opener = getOpener(header)  
op = opener.open(url)  
data = op.read()  
data = ungzip(data)     # ��ѹ  
_xsrf = getXSRF(data.decode())  
#post���ݽ��պʹ����ҳ�棨����Ҫ�����ҳ�淢�����ǹ����Post���ݣ�  
url += 'login/email'  
id = ''  
password = ''  
#����Post���ݣ���Ҳ�Ǵ�ץ��İ�������ó��ġ�  
postDict = {  
        '_xsrf':_xsrf, #�������ݣ���ͬ��վ���ܲ�ͬ    
        'email': id,  
        'password': password,  
        'rememberme': 'y'  
}  
#��Ҫ��Post���ݱ���    
postData = urllib.parse.urlencode(postDict).encode()  
op = opener.open(url, postData)  
data = op.read()  
data = ungzip(data)  
   
print(data.decode())      