import pytest
from conftest import driver
# import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Optional: specify the path to your ChromeDriver
# service = Service('/path/to/chromedriver')
# driver = webdriver.Chrome(service=service)


class Automation_init():
    url = "https://www.example.com"
    # driver = webdriver.Chrome()
    def init_driver(self, driver):
        # If chromedriver is in PATH

        # Open Google
        driver.get(self.url)



driver1 = Automation_init()
# driver = Automation_init.driver
# @allure.feature("User Authentication")
# @allure.story("Login Functionality")
# # @allure.severity(allure.severity_level.CRITICAL)
# @pytest.mark.test1
# def test_sampleui_123():
#     with allure.step("Enter valid credentials"):
#         driver1.init_driver()
#         driver.implicitly_wait(3)
#         driver.quit()



# @pytest.mark.test1
# def test_sampleui_1234():
#     with allure.step("Enter valid credentials"):
#         driver1.init_driver()
#         driver.implicitly_wait(3)
#         time.sleep(3)
#         try:
#             # wait 10 seconds before looking for element
#             element = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//*[@title='Search']"))
#             )
#         finally:
#             # else quit
#             driver.quit()


@pytest.mark.test1
def test_sampleui_1234(driver):
    #with allure.step("Enter valid credentials"):
    # driver1.init_driver(driver)
    driver.implicitly_wait(3)
    # time.sleep(3)
    try:
        # wait 10 seconds before looking for element
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Example Domain']"))
        )
    finally:
        pass
        # else quit
        # driver.quit()


