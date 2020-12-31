from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_location="/usr/local/bin/chromedriver"
binary="/usr/bin/google-chrome"

driver = webdriver.Chrome(driver_location)



driver.get("http://40.117.91.181:8080/petclinics/owners/new")

driver.implicitly_wait(20)
driver.maximize_window()

#fill out form
driver.find_element_by_name("firstName").Send_keys("John");
driver.find_element_by_name("lastName").Send_keys("Doe");
driver.find_element_by_name("address").Send_keys("Street X");
driver.find_element_by_name("city").Send_keys("Amsterdam");
driver.find_element_by_name("telephone").Send_keys("0612345678");


#Act
driver.find_element_by_css_selector('button.btn btn default').click()
driver.implicitly_wait(5)

driver.find_element_by_css_selector('a.btn btn default').click()
driver.implicitly_wait(5)

driver.find_element_by_name("name").Send_keys("Pet1");
driver.find_element_by_name("birthDate").Send_keys("2020/12/11");
driver.find_element_by_name("type").Send_keys("bird");

driver.find_element_by_css_selector('button.btn btn default').click()
driver.implicitly_wait(5)

#Assert
#Assert.IsTrue(driver.PageSource.Contains(firstName));

#quit driver
driver.quit()
