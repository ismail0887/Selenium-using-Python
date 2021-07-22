from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\SeleniumWebdriver\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Ismail")

driver.find_element_by_name("email").send_keys("ismail123@gmail.com")

driver.find_element_by_id("exampleInputPassword1").send_keys("ismail@123")

driver.find_element_by_id("exampleCheck1").click()