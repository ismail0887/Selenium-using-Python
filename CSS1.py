from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\SeleniumWebdriver\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("input[name='name']").send_keys("ISMAIL")