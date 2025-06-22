import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from project_orange.pages.login_page import LoginModule
from project_orange.utils.logger import get_logger
from project_orange.utils.driver_setup import get_driver

logger=get_logger("TestLogin")
def test_login():
    logger.info("Starting OrangeHRM login test")
    driver=get_driver()
    try:
        login=LoginModule(driver)
        logger.info("Navigating to login page")
        login.load()
        logger.info("Entering username and password")
        login.user_pass("Admin","admin123")
        time.sleep(3)
        current_url=driver.current_url
        if "dashboard" in current_url:
            logger.info("Login successful! Current URL:"+current_url)
        else:
            logger.info("Login may have failed. Current URL:" + current_url)

        driver.save_screenshot("screenshots/login_result.png")
        logger.info("Screenshot saved to screenshots/login_result.png")

    except Exception as e:
        logger.error("An error occurred")
        logger.exception(e)
    finally:
        driver.quit()
        logger.info("driver closed,test completed")