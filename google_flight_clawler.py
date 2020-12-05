import time
from selenium import webdriver
import selenium.common
import pickle
from bs4 import BeautifulSoup
from lxml import etree

candidates = []
companies_i_want = ['东航']

driver = webdriver.Chrome(
    'D:\install\Anaconda\Scripts\chromedriver.exe')
for month in range(5, 7):
    day_list = []
    if month == 5:
        day_list = range(12, 32)
    else:
        day_list = range(1, 31)
    for day in day_list:
        driver.get('https://www.google.com/flights?lite=0#flt=/m/02dtg./m/06wjf.2020-0%d-%d;c:USD;e:1;sd:1;t:f;tt:o' % (
            month, day))
        time.sleep(.3)
        date = str(month) + '/' + str(day)
        print(date)
        try:
            ol = driver.find_elements_by_css_selector('ol.gws-flights-results__result-list')
        except selenium.common.exceptions.NoSuchElementException:
            print('nothing found')
            continue
        for o in ol:
            li = o.find_elements_by_tag_name('li')
            print(len(li))
            for l in li:
                print(l.text)
                try:
                    companies = l.find_element_by_css_selector('span.gws-flights__ellipsize')
                except selenium.common.exceptions.NoSuchElementException:
                    continue
                company_list = companies.find_elements_by_css_selector('span')
                if company_list[-1].text in companies_i_want:
                    candidates.append(date + '\n' + l.text)

print('candidates:')

for candidate in candidates:
    print(candidate)
    print('')