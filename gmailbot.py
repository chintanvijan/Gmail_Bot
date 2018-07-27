from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
from getdriver import driver1
import time
def login():
	driver = driver1.drive()
	driver.get("http://www.gmail.com/")
	#driver.get_screenshot_as_file("ss.png")
	#driver.implicitly_wait(10)
	#u = driver.current_url
	#print(u)
	#w=driver.page_source
	#print(w)

	driver.find_element_by_id('Email').send_keys("chintanvijan@gmail.com")


	driver.find_element_by_id("next").click()
	time.sleep(4)
	#w=driver.page_source
	#print(w)
	driver.find_element_by_id("Passwd").send_keys("mushimushi")
	driver.find_element_by_id("signIn").click()
	#print("Success")
	time.sleep(4)
	
	driver.find_element_by_xpath("//*[contains(text(), 'COMPOSE')]").click()
	time.sleep(4)
	#w=driver.page_source
	#print(w)
	driver.find_element_by_name("to").send_keys("chintanvijan1998@gmail.com")
	driver.find_element_by_name("subjectbox").send_keys("Subject")

	driver.find_element_by_xpath('//div[@id=":nk"]').send_keys("Content!")
	driver.find_element_by_xpath("//div[@id=':m5']").click()
	time.sleep(2)

	driver.find_element_by_xpath("//*[@id='gb']/div[1]/div[1]/div/div[5]/div[1]/a/span").click()
	time.sleep(2)
	driver.find_element_by_xpath("//*[@id='gb_71']").click()
	driver.quit()
	#display.stop()
	#driver.find_element_by_id(":nk").click()
login()