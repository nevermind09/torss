from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import codecs
import random

######################  Setting  ##############################
LOCAL_URL = 'http://127.0.0.1:8910/'
TORRENT_SITE_URL = 'http://www.tfreeca22.com'
BO_TABLE_NAME = 'tdrama'
BO_TABLE_NAME_Xpath = './/div[@class="list_subject"]/a[2]'
INIT_START_NUM = 10
###############################################################

startNum = 0
endNum = 0
tempXML = ""

class inti:
    def __init__(self,startNum,endNum):
        self.startNum = startNum
        self.endNum = endNum

def find_str(s, char):
    index = 0
    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index
            index += 1
    return -1

def tfreecaXML(x,y,z):
    driver = webdriver.Remote(command_executor=LOCAL_URL, desired_capabilities=DesiredCapabilities.PHANTOMJS)
    url = TORRENT_SITE_URL+'/info.php?bo_table='+BO_TABLE_NAME+'&wr_id='+str(x)
    driver.get(url)
    if x == y:
        try:
            text1=driver.find_element_by_xpath('.//div')
            text2=driver.find_element_by_xpath('.//a')
            print(text1.text.replace(".torrent",""))
            print(text2.text)
            z="\t\t<item>\n\t\t\t<title>"+str(text1.text.replace(".torrent",""))+"</title>\n\t\t\t<link>"+str(text2.text)+"</link>\n\t\t</item>\n"+z
            z= "<rss version='2.0'>\n\t<channel>\n"+z+"\t</channel>\n</rss>"
        except:
            z= "<rss version='2.0'>\n\t<channel>\n"+z+"\t</channel>\n</rss>"
        NestartNum = str(int(y)-1)
        bbsFileWrite(NestartNum)
        makeXMLRSS(z)
    else:
        try:
            text1=driver.find_element_by_xpath('.//div')
            text2=driver.find_element_by_xpath('.//a')
            print(text1.text.replace(".torrent",""))
            print(text2.text)
            if  random.random()*10 < 1 :
                ti=1
            else:
                ti=random.random()*10
            sleep(ti)
            z="\t\t<item>\n\t\t\t<title>"+str(text1.text.replace(".torrent",""))+"</title>\n\t\t\t<link>"+str(text2.text)+"</link>\n\t\t</item>\n"+z
            return tfreecaXML(x+1,y,z)
        except:
            return tfreecaXML(x+1,y,z)        
        

def tfreecaGenNum():
    driver = webdriver.Remote(command_executor=LOCAL_URL, desired_capabilities=DesiredCapabilities.PHANTOMJS)
    driver.get(TORRENT_SITE_URL+'/board.php?mode=list&b_id='+BO_TABLE_NAME+'&page=1')
    dd=driver.find_elements_by_xpath(BO_TABLE_NAME_Xpath)
    maxNumTemp=dd[0].get_attribute('href')
    try:
        t=open(BO_TABLE_NAME+"_bbsnum.txt",'r').read().splitlines()
        startNum = t[0]
        endNum = str(maxNumTemp)[find_str(str(maxNumTemp),'&id=')+len('&id='):find_str(str(maxNumTemp),'&page')]
    except:
        endNum = str(maxNumTemp)[find_str(str(maxNumTemp),'&id=')+len('&id='):find_str(str(maxNumTemp),'&page')]
        startNum = str(int(endNum) - INIT_START_NUM)
        print(startNum)
    return(startNum,endNum)

def makeXMLRSS(z):
    w=codecs.open(BO_TABLE_NAME+"_rss.xml",'w',"utf-8")
    w.write(z)
    w.close()

def bbsFileWrite(g):
    w=open(BO_TABLE_NAME+"_bbsnum.txt",'w')
    w.write(g)
    w.close()
    

try:
    t=open(BO_TABLE_NAME+"_bbsnum.txt",'r').read().splitlines()
    t[0]
    tfreecaGen=tfreecaGenNum()
    inti.startNum=tfreecaGen[0]
    inti.endNum=tfreecaGen[1]
    tfreecaXML(int(inti.startNum),int(inti.endNum),tempXML)
except:
    w=open(BO_TABLE_NAME+"_bbsnum.txt",'w')
    w.write(tfreecaGenNum()[0])
    w.close()
    tfreecaGen=tfreecaGenNum()
    inti.startNum=tfreecaGen[0]
    inti.endNum=tfreecaGen[1]
    tfreecaXML(int(inti.startNum),int(inti.endNum),tempXML)
