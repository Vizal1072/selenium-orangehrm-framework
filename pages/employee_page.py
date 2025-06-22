import time

from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
class EmployeePage:
    def __init__(self,driver):
        self.driver=driver
        self.pim=(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        self.add_button=(By.CSS_SELECTOR,"button[class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.name=(By.XPATH,"//input[@placeholder='First Name']")
        self.last=(By.XPATH,"//input[@placeholder='Last Name']")
        self.save=(By.XPATH,"//button[@type='submit']")

    def add_employee(self,first,last):
        wait=WebDriverWait(self.driver, 15)
        link1 = wait.until(
                ec.element_to_be_clickable(self.pim))
        self.driver.execute_script("arguments[0].click();", link1)
        link2 = wait.until(
                ec.element_to_be_clickable(self.add_button))
        self.driver.execute_script("arguments[0].click();", link2)

        fname = wait.until(ec.element_to_be_clickable(self.name))
        fname.send_keys(first)

        lname = wait.until(ec.element_to_be_clickable(self.last))
        lname.send_keys(last)

        link=wait.until(ec.element_to_be_clickable(self.save))
        self.driver.execute_script("arguments[0].click();", link)
        time.sleep(15)
