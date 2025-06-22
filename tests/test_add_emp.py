
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from project_orange.pages.login_page import LoginModule
from project_orange.utils.logger import get_logger
from project_orange.utils.driver_setup import get_driver
from project_orange.pages.employee_page import EmployeePage
import time
logger=get_logger("Test_Emp")
def test_add_emp():
    logger.info("Starting OrangeHRM login test")
    driver=get_driver()
    try:
        login = LoginModule(driver)
        logger.info("Navigating to login page")
        login.load()
        logger.info("Entering username and password")
        login.user_pass("Admin", "admin123")
        time.sleep(3)
        current_url = driver.current_url
        if "dashboard" in current_url:
            logger.info("Login successful! Current URL:" + current_url)
        else:
            logger.info("Login may have failed. Current URL:" + current_url)

        driver.save_screenshot("screenshots/login_result.png")
        logger.info("Screenshot saved to screenshots/login_result.png")

        emp=EmployeePage(driver)
        logger.info("Navigating to login page")
        logger.info("Entering first name and last name")
        emp.add_employee("john","doe")
        time.sleep(5)
        current_url1=driver.current_url
        if "john" in current_url1 and "doe" in current_url1 :
            logger.info("employee added! Current URL:" + current_url)
        else:
            logger.info("addition failed. Current URL:" + current_url)

        driver.save_screenshot("screenshots/employee_added.png")
        logger.info("Screenshot saved to screenshots/login_result.png")

    except Exception as e:
        logger.error("An error occurred")
        logger.exception(e)
