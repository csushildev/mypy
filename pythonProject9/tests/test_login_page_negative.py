import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:
    @pytest.mark.negative
    @pytest.mark.login
    def test_negative_scenario(self, driver):
        # driver = webdriver.Chrome()
        # time.sleep(3)
        driver.get("https://practicetestautomation.com/practice-test-login/")
        username_locator = driver.find_element(By.XPATH, "/html//input[@id='username']")
        username_locator.send_keys("unauthstudent")
        password_locator = driver.find_element(By.XPATH, "/html//input[@id='password']")
        password_locator.send_keys("Password123")
        submit_locator = driver.find_element(By.XPATH, "/html//button[@id='submit']")
        submit_locator.click()
        login_error_locator = driver.find_element(By.XPATH, "//div[@id='error']")
        assert login_error_locator.is_displayed()
        err_message = login_error_locator.text
        assert err_message == "Your username is invalid!", "Incorrect Username Test Passed"

        # login_message_locator = driver.find_element(By.XPATH, "//div[@id='content']//p")
        # actual_message = login_message_locator.text
        # assert actual_message.__contains__("Congratulations")
