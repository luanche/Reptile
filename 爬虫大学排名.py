import requests
from bs4 import BeautifulSoup
allUniv = []
data = []
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd)==0:
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)
        allUniv.append(singleUniv)
def printUnivList(num):
    print("{0:^5}\t{1:^15}\t{2:>6}\t{3:<8}\t{4:^8}".format("排名","学校名称","省份","总分","培养规模",chr(12288)))
    for i in range(num):
        u=allUniv[i]
        print("{0:^5}\t{1:^15}\t{2:>6}\t{3:<10}\t{4:^10}".format(u[0],u[1],u[2],u[3],u[6],chr(12288)))
        data.append([u[0],u[1],u[2],u[3],u[6]])
def write_data(data,name):
    fw = open(name,"w")
    fw.write("排名,"+"学校名称,"+"省份,"+"总分,"+"培养规模\n")
    for item in data:
        fw.write(",".join(item) + "\n")
    fw.close()
def main(num):
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html,"html.parser")
    fillUnivList(soup)
    printUnivList(num)
    write_data(data,'rank.csv')
main(10)
    
