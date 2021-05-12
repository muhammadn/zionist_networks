#!/usr/bin/env python3

from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36")
driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)

driver.get("https://bgp.he.net/country/IL")
page_source = driver.page_source

soup = BeautifulSoup(page_source, features="lxml")
asns = soup.find("table", id="asns").find("tbody").find_all("a")

for asn in asns:
    driver.get("https://bgp.he.net/" + asn.text + "#_prefixes")
    time.sleep(5)
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, features="lxml")
    # get all IPv4 networks, can be tweaked for IPv6
    result = soup.find("table", id="table_prefixes4").find("tbody").find_all("a")
    for i in result:
        f.write(i.text + "\n")
        print(i.text)
