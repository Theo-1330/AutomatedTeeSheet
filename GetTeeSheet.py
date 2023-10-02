from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
from pyvirtualdisplay import Display
from easyprocess import EasyProcess

d = Display(visible=0, size=(1920,1080))
d.start()
s = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
today = datetime.date.today()

# replace with your own string values
login = [ACCOUNT_NAME, USERNAME, PASSWORD] 

driver.get('https://app.golfnowone.com/App/SpaAdmin/Orders/PointOfSale.aspx')

account = driver.find_element(By.NAME, 'ctl00$content$txtAccountName')
account.send_keys(login[0])

user = driver.find_element(By.NAME, 'ctl00$content$txtUsername')
user.send_keys(login[1])

pwd = driver.find_element(By.NAME, 'ctl00$content$txtPassword')
pwd.send_keys(login[2] + Keys.RETURN)

wait = WebDriverWait(driver, 20)
element = wait.until(EC.presence_of_element_located((By.ID, 'ctl00_ctl00_content_content_ucOrderWorkflow_ucCashRegisterDialog_upnlCashRegisterSelection')));
if EC.presence_of_element_located((By.ID, 'ctl00_ctl00_content_content_ucOrderWorkflow_ucCashRegisterDialog_upnlCashRegisterSelection')):
	action = ActionChains(driver)
	action.key_down(Keys.CONTROL).send_keys('SUBTRACT').key_up(Keys.CONTROL).perform()
	action.key_down(Keys.CONTROL).send_keys('SUBTRACT').key_up(Keys.CONTROL).perform()
	radio = driver.find_element(By.CSS_SELECTOR,"div.area:nth-child(1) > div:nth-child(2) > label:nth-child(1) > span:nth-child(2)").click()
	btn = driver.find_element(By.ID, "ctl00_ctl00_content_content_ucOrderWorkflow_ucCashRegisterDialog_btnChangeRegister").click()
	time.sleep(15)
	
else:
	print("not detected")
time.sleep(5)

driver.get('https://app.teesheet-us-west.golfnowone.com/ca_alhambra/print_daily_booking_sheet.php?course_id=1&d_date='+str(today))
time.sleep(10)

driver.find_element(By.CSS_SELECTOR, "body > div > form > table > tbody > tr:nth-child(18) > td > input[type=checkbox]:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, "body > div > form > table > tbody > tr:nth-child(19) > td > input").click()
time.sleep(20)
