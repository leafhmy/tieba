import urllib.request
import urllib.error
import re
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
#opener添加为全局
urllib.request.install_opener(opener)
key="金融"
try:
    for page in range(1,11):
        data=urllib.request.urlopen("http://tieba.baidu.com/f/search/res?&kw=福建江夏学院&qw="+key+"&pn="+str(page)).read().decode("utf-8","ignore")
        pat='href="(.*?)class="bluelink" target="_blank" >'
        url=re.compile(pat).findall(data)
        purl="tieba.baidu.com"+str(url)
        tdata=urllib.request.urlopen("purl").read().decode("utf-8","ignore")
        for i in range(0,len(purl)):
            fh=open("D:/Download/第"+str(i)+"篇.txt","wb")
            fh.write(tdata)
            fh.close()
except urllib.error.URLError as e:
    if hasattr(e,"code"):
            print(e.code)
    if hasattr(e,"reason"):
            print(e.reason)
except Exception as e:
    print(e)
