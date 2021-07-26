import sys
import time
from bs4 import BeautifulSoup
from selenium import webdriver

driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
root = "https://www.google.com/"
url = "https://www.google.com/search?q=hdfc&rlz=1C1CHBF_enIN855IN856&biw=2048&bih=972&sxsrf=ALeKk01uXoYzhgyOm6VhkA2LkuH9pLLizg%3A1626762392480&source=lnt&tbs=cdr%3A1%2Ccd_min%3A12%2F1%2F2020%2Ccd_max%3A12%2F31%2F2020&tbm=nws"


def news(url):
    driver.get(url)
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    for item in soup.find_all('div', attrs={'class': 'dbsr'}):
        title = (item.find('div', attrs={'class': 'JheGif nDgy9d'})).get_text()
        description = (item.find('div', attrs={'class': 'Y3v8qd'})).get_text()
        mydate = (((item.find('span', attrs={'class': 'WG9SHc'}))).find('span')).get_text()
        mydate = mydate.replace(",", "")
        title = title.replace(",", "")
        description = description.replace(",", "")
        description = description.replace("\n", " ")
        title = title.replace("\n", " ")
        document = open("data.csv", "a", encoding="utf-8")
        document.write("{}, {}, {} \n".format(mydate, title, description))
        document.close()
    next = soup.find('a', attrs={'id': 'pnnext'})
    try:
        next = (next['href'])
        url = root + next
    except TypeError:
        sys.exit()
    news(url)


news(url)
