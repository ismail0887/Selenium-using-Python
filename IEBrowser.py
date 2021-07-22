from selenium import webdriver
#browser exposes an executable file
#Through selenium test we need to invoke the executable file
driver = webdriver.Ie(executable_path="C:\SeleniumWebdriver\IEDriverServer.exe")

driver.get("https://facebook.com/")

print(driver.title) #to retrive title of webpage
print(driver.current_url) #to retrive current url
driver.get("https://www.cricbuzz.com/cricket-schedule/upcoming-series/international")
driver.maximize_window()
driver.back()
driver.maximize_window()
driver.refresh()
driver.close() # it will close current browser window