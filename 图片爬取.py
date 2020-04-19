import urllib.request
import re
import os
import urllib
imglist = []
def getHtml(url):
    try:
        page = urllib.request.urlopen(url)
        html = page.read()
        return html.decode('UTF-8')
    except:
        return ""
def getImg(html):
    reg = r'src="(.+?\.jpg)" size'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    path = 'D:\\test'  
    if not os.path.isdir(path):  
        os.makedirs(path)  
    for item in imglist:  
        urllib.request.urlretrieve(item,'{0}\\{1}.jpg'.format(path,x))
        x += 1
def main():
    url = "http://tieba.baidu.com/p/5491967088"
    html = getHtml(url)
    print("Downloading...")
    getImg(html)
    print(r"Done!Check the D:\test\ ")
main()
