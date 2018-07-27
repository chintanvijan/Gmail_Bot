from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
import time

def drive():
	chrome_options = Options()
	#Chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application"
	WINDOW_SIZE = "1400,800"
	chrome_options.add_argument("start-maximised")
	chrome_options.add_argument("disable-infobars")
	chrome_options.add_argument("disable-extensions")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
	#chrome_options.binary_location(Chrome_path)
	#display = Display(visible=0,size=(600,800))
	#display.start()
	driver = webdriver.Chrome(chrome_options=chrome_options)
	
	#driver.get_screenshot_as_file("ss.png")
	#driver.implicitly_wait(10)
	#u = driver.current_url
	#print(u)
	#w=driver.page_source
	#print(w)
	return driver