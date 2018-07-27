from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
from getdriver import driver1
import time
from login_gmail import gmailbot as gb 

def exec():
	gb.login()
exec()