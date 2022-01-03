from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def set_options():
    chrome_options = Options()
    # Add other options here
    """
    Examples:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")
    """
    return chrome_options


# Used for finding elements with the Selenium library
def read_XPATH(self,xpath, attr):
    try:
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    except Exception as e:
        print(f"Caught Exception: {e}")
    data = self.driver.find_element(By.XPATH, xpath).get_attribute(attr);
    return data

def send_keys_to_xpath(driver, keys, xpath):
	try:
		WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
	except Exception as e:
		print(f"Caught Exception: {e}")
	driver.find_element(By.XPATH, xpath).send_keys(keys)
	
def click_on_xpath(driver,xpath):
	try:
		WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
	except Exception as e:
		print(f"Caught Exception: {e}")
	driver.find_element(By.XPATH, xpath).click()