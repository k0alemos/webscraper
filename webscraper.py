from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()

# options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("https://carlislehomes.com.au/home-designs/#Promotion:both/HomeName:/HomeRange:both,Affinity/Storey:all/Bed:all/MinBlockWidth:all/MinBlockDepth:all/Price:all~all/Bath:/ExtraOptions:/HomeSeries:/HouseSize:all~all/")
# print(driver.page_source)

test = driver.find_element(By.CLASS_NAME,"filter-results-holder")
testagain = test.get_attribute('innerHTML')
print("THIS IS THE PRINT ********",testagain)
driver.quit()



