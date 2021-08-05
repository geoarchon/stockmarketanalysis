import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup 
from newspaper import Article

def getDate(url):
    article = Article(url)
    article.download()
    article.parse()
    return(article.publish_date)
    # function to fetch some of the dates where x days ago, x weeks ago appears

def news(url):
    driver.get(url)
    time.sleep(10)
    # Parse content with BeautifulSoup
    soup=BeautifulSoup(driver.page_source,'html5lib')
    #print(soup.prettify()) to check the raw html
    for item in soup.find_all('div', attrs={'class':'dbsr'}):
        #raw_link = (item.find('a', href=True)['href'])
        #link = raw_link#.split("/url?q=")[1].split("&sa=U&")[0]
        title=(item.find('div', attrs={'class': 'JheGif nDgy9d'})).get_text()
        description=(item.find('div', attrs={'class': 'Y3v8qd'})).get_text()
        mydate=(((item.find('span', attrs={'class':'WG9SHc'}))).find('span')).get_text()
        #format the data
        mydate=mydate.replace(",","")
        title=title.replace(",","")
        description=description.replace(",","")
        description=description.replace("\n"," ")
        title=title.replace("\n"," ")
        #to read and write 
        document = open("data2.csv", "a",encoding="utf-8")
        document.write("{}, {}, {} \n".format(mydate, title, description))
        document.close()
    next = soup.find('a', attrs={'id':'pnnext'})
    try:
        next = (next['href'])
        url = root + next
    except TypeError:
        #sys.exit() #exit when eof is reached
        return
    news(url) # recursive call to cover all pages of given search term

month1 = 7 # give starting month
month2 = 8+1 # give ending month and add 1 to it 
# news article info will be collected from month1 to month2 (both inclusive)
d1=5
m1=0
y1=2021
d2=5
m2=0
y2=2021
flag=0

for x in range(month1,month2):
    #flag=flag+1
    #if(flag == 2):
        #break
    # uncomment the previous 2 lines if you want to just test the code with one month of data
    driver_path = 'chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    m1=x
    m2=x+1
    root = "https://www.google.com/"
    url = "https://www.google.com/search?q=hdfc&rlz=1C1CHBF_enIN855IN856&biw=2048&bih=972&sxsrf=ALeKk01uXoYzhgyOm6VhkA2LkuH9pLLizg%3A1626762392480&source=lnt&tbs=cdr%3A1%2Ccd_min%3A"+str(m1)+"%2F"+str(d1)+"%2F"+str(y1)+"%2Ccd_max%3A"+str(m2)+"%2F"+str(d2)+"%2F"+str(y2)+"&tbm=nws"
    news(url) # initial call to function