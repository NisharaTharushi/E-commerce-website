from selenium.webdriver.common.by import By
import time


class Login():
    def __init__(self, driver):
        self.driver = driver


    # locators
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")

    
    print("---- Login page ----")
    
    # login form
    def login(self, email, password):
        print("-- Login Form --")
        
        email_input = self.driver.find_element(*Login.LOGIN_EMAIL_INPUT)
        self.driver.execute_script("arguments[0].scrollIntoView();", email_input)
        email_input.send_keys(email)
        print("email input value:",email_input.get_attribute("value"))
        
        password_input = self.driver.find_element(*Login.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(password)
        print("password input value:",password_input.get_attribute("value"))
        
        login_button = self.driver.find_element(*Login.LOGIN_BUTTON)
        self.driver.execute_script("arguments[0].click();", login_button)
        print("login button clicked ")
        print("open page current url:",self.driver.current_url)
        time.sleep(2)
        print("")


        # check current url
        if self.driver.current_url == "https://www.automationexercise.com/":
            print("Login successful page opened. checked with current url")
        else:
            print("Login failed")


