
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
chromeOptions.headless = True
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=chromeOptions)
driver.get("http://168.62.62.94:8080/petclinics/owners/new")

driver.implicitly_wait(20)
driver.maximize_window()

#fill out form
driver.find_element_by_name("firstName").send_keys("John");
driver.find_element_by_name("lastName").send_keys("Doe");
driver.find_element_by_name("address").send_keys("Street X");
driver.find_element_by_name("city").send_keys("Amsterdam");
driver.find_element_by_name("telephone").send_keys("0612345678");


#Act
driver.find_element_by_css_selector('button.btn btn-default').click()
driver.implicitly_wait(5)

driver.find_element_by_css_selector('a.btn btn-default').click()
driver.implicitly_wait(5)

driver.find_element_by_name("name").send_keys("Pet1");
driver.find_element_by_name("birthDate").send_keys("2020/12/11");
driver.find_element_by_name("type").send_keys("bird");

driver.find_element_by_css_selector('button.btn btn-default').click()
driver.implicitly_wait(5)

#Assert
#Assert.IsTrue(driver.PageSource.Contains(firstName));

#quit driver
driver.quit()


