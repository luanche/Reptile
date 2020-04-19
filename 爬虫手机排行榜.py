import requests
from bs4 import BeautifulSoup
import re
allphone = []
data = []
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = 'gbk'
        return r.text
    except:
        return ""
def fillPhoneList(soup,num):
    allphone = soup.find_all('div',{'class':'rank-list__item clearfix'})
    for i in range(num):
        eachphone = []
        eachdata = allphone[i].find_all('div',{'class':'rank__number'})
        if i == 0:
            eachphone.append('1')
        else :
            eachphone.append(eachdata[0].string)
        eachdata = allphone[i].find_all('div',{'class':'rank__name'})
        eachphone.append(re.sub('（.*?）','',eachdata[0].string))
        eachdata = allphone[i].find_all('div',{'class':'rank__price'})
        eachphone.append(eachdata[0].string.strip().replace('￥',''))
        eachdata = allphone[i].find_all('div',{'class':'score clearfix'})
        eachdata = eachdata[0].find_all('span')
        eachphone.append(eachdata[0].string.replace('分',''))
        data.append(eachphone)
def printUnivList():
    print("{0:^2}\t{1:^18}\t{2:^10}\t{3:^3}".format("排名","型号","价格（元）","评分（10分）",chr(12288)))
    for u in data:
        print("{0:^2}\t{1:^18}\t{2:^10}\t{3:^3}".format(u[0],u[1],u[2],u[3],chr(12288)))
def write_data(data,name):
    fw = open(name,'w')
    fw.write("排名,"+"型号,"+"价格（元）,"+"评分（10分）\n")
    for item in data:
        fw.write(",".join(item) + "\n")
    fw.close()
def main(num):
    url = 'http://top.zol.com.cn/hot/cell_phone.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html,"html.parser")
    fillPhoneList(soup,num)
    printUnivList()
    write_data(data,'phonerank.csv')
main(20)
