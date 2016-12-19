import os;
import sys;
import urllib.request
import requests


'''webheader2 = {  
    'Connection': 'Keep-Alive',  
    'Accept': 'text/html, application/xhtml+xml, */*',  
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding':"gzip, deflate", 
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',  
    #'Accept-Encoding': 'gzip, deflate',  
    'Host': '',  
    'DNT': '1'  
    }'''

def CheckArgs():
    if(len(sys.argv) < 3):
        print ('Usage: python ImgSearch.py [Keyword] [DownloadDir] [Pages=1]');
        return False;
    return True;

def Download(url_list):
    if(os.path.exists(sys.argv[2]) == False):
        os.mkdir(sys.argv[2]);   
   
    for url in url_list:
        print ('Downloading from %s' % url);
        filename = os.path.split(url)[1]
        filepath = os.path.join(sys.argv[2], '%s' % filename);
        try:
            urllib.request.urlretrieve(url, filepath);
        except:
            print ("Download fail");
    print ('DownLoad done')
    return ;

def Request(param):
    #searchurl = 'http://image.baidu.com/search/avatarjson';
    searchurl = 'http://image.baidu.com/search/acjson';
    response = requests.get(searchurl, params=param);
    #print (response.url)
    json = response.json()['data'];
    url_list = []

    for i in range(0, len(json)):
        if ('hoverURL' in json[i].keys()):       
            url_list.append(json[i]['hoverURL'])           
    Download(url_list);  
    return ;

def file_count(dirname,filter_types=[]):
    count=0
    filter_is_on=False
    if filter_types!=[]: filter_is_on=True
    for item in os.listdir(dirname):
        abs_item=os.path.join(dirname,item)
        #print (item)
    if os.path.isdir(abs_item):
        #Iteration for dir
        count+=file_count(abs_item,filter_types)
    elif os.path.isfile(abs_item):
        if filter_is_on:
            #Get file's extension name
            extname=os.path.splitext(abs_item)[1]
            if extname in filter_types:
                count+=1
        else:
            count+=1
    return count

def Search():
    params = {
        'tn':'resultjson_com',
        'ipn':'rj',
        'ct':'201326592',
        'is':'',
        'fp':'result',
        'queryWord':sys.argv[1],
        'cl':'2',
        'lm':'-1',
        'ie':'utf-8',
        'oe':'utf-8',
        'adpicid':'',
        'st':'-1',
        'z':'',
        'ic':'0',
        'word':sys.argv[1],
        's':'',
        'se':'',
        'tab':'',
        'width':'',
        'height':'',
        'face':'0',
        'istype':'2',
        'qc':'',
        'nc':'1',
        'fr':'',
        'rn':'30',
        'gsm':'1e00000000001e',
        '1481765319730':''
        };    
    
    if(len(sys.argv) == 4):
        pages = int(sys.argv[3]);
    else:
        pages = 1;

    for i in range(1, pages):
        params['pn'] = '%d' % (i*30);
        print (params['pn'])
        Request(params);
    return ;

if __name__ == '__main__':
    if(CheckArgs() == False):
        sys.exit(-1);
    Search();
print ('Total Images:%d' % file_count(sys.argv[2]));