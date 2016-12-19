#coding=utf-8
import re   
import os 
import urllib.request
import requests

keyWorld=""


#baseurl="http://image.baidu.com/search/index?ct=201326592&cl=2&lm=-1&tn=baiduimage&ie=utf-8&word="
baseurl="http://pic.yesky.com/233/39488233_20.shtml"
webheader1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}  
webheader2 = {  
    'Connection': 'Keep-Alive',  
    'Accept': 'text/html, application/xhtml+xml, */*',  
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding':"gzip, deflate", 
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',  
    #'Accept-Encoding': 'gzip, deflate',  
    'Host': '',  
    'DNT': '1'  
    } 
targetDir = r"D:\PythonWorkPlace\PicOther"

def destFile(path):    
    if not os.path.isdir(targetDir):    
        os.mkdir(targetDir)    
    pos = path.rindex('/')    
    t = os.path.join(targetDir, path[pos+1:])    
    return t 

def saveData(data):
    save_path = 'D:\\temp.out'  
    f_obj = open(save_path, 'wb')
    f_obj.write(data)  
    f_obj.close()
    print ('Save sucess')
    
def getHtml():
    weburl=baseurl+keyWorld
    print(weburl)
    req = urllib.request.Request(url=weburl, headers=webheader2)
    page = urllib.request.urlopen(req)
    html = page.read()
    #saveData(html)
    return html
    
def getImg(html):
    reg = r'"(http.+?\.jpg)"'
    imgre = re.compile(reg)
    html = html.decode('utf-8')
    imglist = re.findall(imgre,html)
    count = 0
    tmpFil = [0, 0]
    for imgurl in imglist:
        print (imgurl)
        filePath = destFile(imgurl)
        if tmpFil[0] == filePath or tmpFil[1] == filePath:
            continue
        tmpFil[count%2] = filePath
        count +=1
        try:
            urllib.request.urlretrieve(imgurl, destFile(imgurl))
        except:  
            print('failed')
    return count


#html = getHtml("http://tieba.baidu.com/p/4871933902")
html = getHtml()

print (getImg(html))