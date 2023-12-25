import time

import pytest
from selenium.webdriver.common.by import By


class TestPositiveScenarios:
    #assert isinstance(pytest.mark.login, object)

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # driver = webdriver.Chrome()
        # time.sleep(3)
        driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        time.sleep(2)
        login_message_locator = driver.find_element(By.XPATH, "//div[@id='content']//p")
        actual_message = login_message_locator.text
        assert actual_message.__contains__("Congratulations")




#BLOCK 1
"""
**** Block one is to test the element locator and browse throught pages. 
but since we dont have success page or url in pega as of now. for login assertion will 
create a block two.

#go to webpage
driver.get("http://localhost:9090/prweb/PRServlet/app/default/beEBp4uRVTogorRwSwWqbOtn9IL2fwdI*/!STANDARD")
time.sleep(3)

#username locator
username_locator = driver.find_element(By.ID, "txtUserID")
username_locator.send_keys("scdev@gms")

#password locator
password_locator = driver.find_element(By.ID, "txtPassword")
password_locator.send_keys("install")

#submit button locator
submit_locator = driver.find_element(By.XPATH, "/html//button[@id='sub']")
submit_locator.click()

actual_url = driver.current_url

if actual_url.__contains__("renewable"):
    print("login to rems was successful")
else:
    print("login to rems failed")

time.sleep(5)
#print(actual_url)
"""

# BLOCK 2




