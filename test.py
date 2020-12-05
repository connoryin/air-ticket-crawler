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

def test():
    controller = Controller.from_port(port=9151)
    controller.authenticate()
    socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9150)
    socket.socket = socks.socksocket

    driver = webdriver.Chrome(
        'D:\install\Anaconda\Scripts\chromedriver.exe')
    print(driver.get('http://checkip.amazonaws.com').text)

if __name__=='__main__':
    test()