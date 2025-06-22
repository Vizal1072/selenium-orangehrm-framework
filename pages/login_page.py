import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginModule:
    def __init__(self,driver):
        self.driver=driver
        self.user_input=(By.XPATH,"//input[@placeholder='Username']")
        self.pass_input=(By.XPATH,"//input[@placeholder='Password']")
        self.login_button=(By.XPATH,"//button[@type='submit']")

    def load(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def user_pass(self,username,password):
        wait=WebDriverWait(self.driver,10)
        user=wait.until(EC.presence_of_element_located(self.user_input))
        passw=self.driver.find_element(*self.pass_input)
        user.send_keys(username)
        passw.send_keys(password)

        link = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.login_button)
        )
        self.driver.execute_script("arguments[0].click();", link)


