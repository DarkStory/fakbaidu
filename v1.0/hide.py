import re
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import urllib.parse
import xlwt
import sqlite3


# pat = re.compile("AA")
# m = pat.search("CBAA")
# print(m)
# ----------------
# m = re.search("asd","asd asdd asd")
# print(m)

# print(re.findall("aa","aakkaakkaakaa"))
# print(re.findall("aa","aakkaakkaakaa"))
# print(re.findall("[A-z]","aakkaakkaakaa"))
# print(re.findall("[A-z]+","aakkaakkaakaa"))
# print(re.sub("a","A","Aaaaaa")) 建议第三个参数前加r

findLink = re.compile(r'<a href="(.*?)">')
findImg = re.compile(r'<img.*src="(.*?)"',re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
# findRating = re.compile(r'')


def getData(baseurl):
    dataList= []
    for i in range(0,10):
        url = baseurl + str(i*25)
        html = askURL(url)

        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"):
            pass
            # print(item)
            data = []
            item = str(item)
            link = re.findall(findLink,item)
            for i in link:
                print (i)



    return dataList

def askURL(url):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36" }
    
    request = urllib.request.Request(url,headers=head)
  
    html = ""
    try:
        
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html



def main():
    pass
  
    baseurl = "https://movie.douban.com/top250?start="
   
    dataList = getData(baseurl)
    # savapath = ".\\top250.xls"






if __name__ == "__main__":
    pass
    main()

