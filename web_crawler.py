from stem import Signal
from stem.control import Controller
import socket
import socks
import requests
from win10toast import ToastNotifier
from selenium import webdriver
import selenium.common
import time
import numpy as np

# controller = Controller.from_port(port=9151)
# controller.authenticate()
# socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9150)
# socket.socket = socks.socksocket

# a = requests.get('http://www.ceair.com/booking/pek-sha-200609_CNY.html').text
# print(a)

toaster = ToastNotifier()

driver = webdriver.Chrome(
    'D:\install\Anaconda\Scripts\chromedriver.exe')
day = []
mayday = ['27', '31']
mayday_armstrong = ['25']
day_armstrong = []
for i in range(1, 16):
    if i < 10:
        day.append('0' + str(i))
    else:
        day.append(str(i))
current = 2

for j in range(2):
    current -= 1
    for _ in range(4):
        if current < 10:
            day_armstrong.append('0' + str(current))
        else:
            day_armstrong.append(str(current))
        current += 2

while True:
    for d in mayday_armstrong:
        driver.get('http://www.ceair.com/booking/ams-sha-2005%s_CNY.html' % d)
        prices = driver.find_elements_by_css_selector('dd.price')
        if len(prices):
            print('May Armstrong')
            print('day:' + d, )
            toaster.show_toast("Ticket found! May Armstrong",
                               'day:' + d,
                               icon_path=None,
                               duration=5,
                               threaded=True)
            exit(0)
        time.sleep(10 + np.random.randint(0, 30))

    for d in day_armstrong:
        driver.get('http://www.ceair.com/booking/ams-sha-2006%s_CNY.html' % d)
        prices = driver.find_elements_by_css_selector('dd.price')
        if len(prices):
            print('June Armstrong')
            print('day:' + d, )
            toaster.show_toast("Ticket found! June Armstrong",
                               'day:' + d,
                               icon_path=None,
                               duration=5,
                               threaded=True)
            exit(0)
        time.sleep(10 + np.random.randint(0, 30))

    for d in mayday:
        driver.get('http://www.ceair.com/booking/nyc-sha-2005%s_CNY.html' % d)
        prices = driver.find_elements_by_css_selector('dd.price')
        if len(prices):
            print('May Newyork')
            print('day:' + d, )
            toaster.show_toast("Ticket found! May Newyork",
                               'day:' + d,
                               icon_path=None,
                               duration=5,
                               threaded=True)
            exit(0)
        time.sleep(10 + np.random.randint(0, 30))

    for d in day:
        driver.get('http://www.ceair.com/booking/nyc-sha-2006%s_CNY.html' % d)
        prices = driver.find_elements_by_css_selector('dd.price')
        if len(prices):
            print('June Newyork')
            print('day:' + d, )
            toaster.show_toast("Ticket found! June Newyork",
                               'day:' + d,
                               icon_path=None,
                               duration=5,
                               threaded=True)
            exit(0)
        time.sleep(10 + np.random.randint(0, 30))
