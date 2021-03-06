import pytest
# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")


class TestPetclinic():
      
  @pytest.fixture()    
  def method(self):
    self.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
    self.vars = {}
  
  def test_teardown(self, method):
    self.driver.quit()
  
  def test_petclinic(self, method):
    # Test name: Petclinic
    # Step # | name | target | value
    # 1 | open | /petclinics/ | 
    self.driver.get("http://20.71.93.170:8086/petclinics/")
    # 2 | setWindowSize | 1450x786 | 
    self.driver.set_window_size(1450, 786)
    # 3 | click | css=li:nth-child(2) > a | 
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > a").click()
    # 4 | click | linkText=Add Owner | 
    self.driver.find_element(By.LINK_TEXT, "Add Owner").click()
    # 5 | click | id=firstName | 
    self.driver.find_element(By.ID, "firstName").click()
    # 6 | type | id=firstName | John
    self.driver.find_element(By.ID, "firstName").send_keys("John")
    # 7 | type | id=lastName | Doe
    self.driver.find_element(By.ID, "lastName").send_keys("Doe")
    # 8 | type | id=address | Street X
    self.driver.find_element(By.ID, "address").send_keys("Street X")
    # 9 | type | id=city | Amsterdam
    self.driver.find_element(By.ID, "city").send_keys("Amsterdam")
    # 10 | type | id=telephone | 0612345678
    self.driver.find_element(By.ID, "telephone").send_keys("0612345678")
    # 11 | click | css=.btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    # 12 | click | linkText=Add New Pet | 
    self.driver.find_element(By.LINK_TEXT, "Add New Pet").click()
    # 13 | click | id=name | 
    self.driver.find_element(By.ID, "name").click()
    # 14 | type | id=name | Pet1
    self.driver.find_element(By.ID, "name").send_keys("Pet1")
    # 15 | click | id=birthDate | 
    self.driver.find_element(By.ID, "birthDate").click()
    # 16 | type | id=birthDate | 2020/12/11
    self.driver.find_element(By.ID, "birthDate").send_keys("2020/12/11")
    # 17 | select | id=type | label=dog
    dropdown = self.driver.find_element(By.ID, "type")
    dropdown.find_element(By.XPATH, "//option[. = 'dog']").click()
    # 18 | click | css=option:nth-child(3) | 
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(3)").click()
    # 19 | click | css=tr:nth-child(3) > td | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td").click()
    print('Title is: ' + self.driver.title)


