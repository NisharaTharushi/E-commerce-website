from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

class SignUp():
    def __init__(self, driver):
        self.driver = driver

    # locators 
    TITLE = (By.TAG_NAME, "h2")
    SIGNUP_NAME_INPUT = (By.XPATH, "//input[@data-qa='signup-name']")
    SIGNUP_EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    GENDER = (By.XPATH, "//input[@id='id_gender2']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    DAY_INPUT = (By.XPATH, "//select[@id='days']")
    MONTH_INPUT = (By.XPATH, "//select[@id='months']")
    YEAR_INPUT = (By.XPATH, "//select[@id='years']")
    NEWSLETTER_INPUT = (By.XPATH, "//input[@id='newsletter']")
    OPTIN_INPUT = (By.XPATH, "//input[@id='optin']")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@id='first_name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='last_name']")
    COMPANY_INPUT = (By.XPATH, "//input[@id='company']")
    ADDRESS_INPUT = (By.XPATH, "//input[@id='address1']")
    ADDRESS2_INPUT = (By.XPATH, "//input[@id='address2']")
    COUNTRY_INPUT = (By.XPATH, "//select[@id='country']")
    STATE_INPUT = (By.XPATH, "//input[@id='state']")
    CITY_INPUT = (By.XPATH, "//input[@id='city']")
    ZIPCODE_INPUT = (By.XPATH, "//input[@id='zipcode']")
    MOBILE_NUMBER_INPUT = (By.XPATH, "//input[@id='mobile_number']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[normalize-space()='Create Account']")
    CONTINUE = (By.XPATH, "//a[normalize-space()='Continue']")
    LOGIN_PAGE_BUTTON = (By.XPATH, "//a[@href='/logout' and @class='fa fa-lock']")
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")


    # signup page and form
    print("---- Signup page ----")
    def sign_up(self, name, email, password,day, month, year, full_name, last_name, company_name, address1, address2, country_name, state, city_name, zipcode, mobile_number):
        print("-- Signup Form --")
        
        name_input = self.driver.find_element(*SignUp.SIGNUP_NAME_INPUT)
        name_input.send_keys(name)
        print("name input value:",name_input.get_attribute("value"))
        time.sleep(2)

        email_input = self.driver.find_element(*SignUp.SIGNUP_EMAIL_INPUT)
        email_input.send_keys(email)
        print("email input value:",email_input.get_attribute("value"))
        time.sleep(2)

        signup_button = self.driver.find_element(*SignUp.SIGNUP_BUTTON)
        self.driver.execute_script("arguments[0].click();", signup_button)
        print("signup button clicked and page opened")
        print("open page current url:",self.driver.current_url)
        time.sleep(6)

        gender = self.driver.find_element(*SignUp.GENDER)
        gender.click()
        print("gender clicked")
        time.sleep(2)

        password_input = self.driver.find_element(*SignUp.PASSWORD_INPUT)
        password_input.send_keys(password)
        print("password input value:",password_input.get_attribute("value"))
        time.sleep(2)

        day_input = self.driver.find_element(*SignUp.DAY_INPUT)
        self.driver.execute_script("arguments[0].scrollIntoView();", day_input)
        option = Select(day_input)
        option.select_by_value(day)
        print("day input value:",day_input.get_attribute("value"))
        time.sleep(2)

        month_input = self.driver.find_element(*SignUp.MONTH_INPUT)
        option = Select(month_input)
        option.select_by_value(month)
        print("month input value:",month_input.get_attribute("value"))
        time.sleep(2)

        year_input = self.driver.find_element(*SignUp.YEAR_INPUT)
        option = Select(year_input)
        option.select_by_value(year)
        print("year input value:",year_input.get_attribute("value"))
        time.sleep(2)

        newsletter_input = self.driver.find_element(*SignUp.NEWSLETTER_INPUT)
        self.driver.execute_script("arguments[0].scrollIntoView();", newsletter_input)
        self.driver.execute_script("arguments[0].click();", newsletter_input)
        print("newsletter input clicked")
        time.sleep(2)

        optin_input = self.driver.find_element(*SignUp.OPTIN_INPUT)
        self.driver.execute_script("arguments[0].scrollIntoView();", optin_input)
        optin_input.click()
        print("optin input clicked")
        time.sleep(2)

        print("Address information")

        first_name_input = self.driver.find_element(*SignUp.FIRST_NAME_INPUT)
        first_name_input.send_keys(full_name)
        print("first name input value:",first_name_input.get_attribute("value"))
        time.sleep(2)

        last_name_input = self.driver.find_element(*SignUp.LAST_NAME_INPUT) 
        last_name_input.send_keys(last_name)
        print("last name input value:",last_name_input.get_attribute("value"))
        time.sleep(2)

        company_input = self.driver.find_element(*SignUp.COMPANY_INPUT)
        company_input.send_keys(company_name)
        print("company input value:",company_input.get_attribute("value"))
        time.sleep(2)

        address_input = self.driver.find_element(*SignUp.ADDRESS_INPUT)
        address_input.send_keys(address1)
        print("address input value:",address_input.get_attribute("value"))
        time.sleep(2)

        address2_input = self.driver.find_element(*SignUp.ADDRESS2_INPUT)
        self.driver.execute_script("arguments[0].scrollIntoView();", address2_input)
        address2_input.send_keys(address2)
        print("address2 input value:",address2_input.get_attribute("value"))
        time.sleep(2)

        country_input = self.driver.find_element(*SignUp.COUNTRY_INPUT)
        option = Select(country_input)
        option.select_by_visible_text (country_name)
        print("country input value:",country_input.get_attribute("value"))
        time.sleep(2)

        state_input = self.driver.find_element(*SignUp.STATE_INPUT)
        state_input.send_keys(state)
        print("state input value:",state_input.get_attribute("value"))
        time.sleep(2)

        city_input = self.driver.find_element(*SignUp.CITY_INPUT)
        city_input.send_keys(city_name)
        print("city input value:",city_input.get_attribute("value"))
        time.sleep(2)

        zipcode_input = self.driver.find_element(*SignUp.ZIPCODE_INPUT)
        zipcode_input.send_keys(zipcode)
        print("zipcode input value:",zipcode_input.get_attribute("value"))
        time.sleep(2)

        mobile_number_input = self.driver.find_element(*SignUp.MOBILE_NUMBER_INPUT)
        mobile_number_input.send_keys(mobile_number)
        print("mobile number input value:",mobile_number_input.get_attribute("value"))
        time.sleep(2)

        create_account_button = self.driver.find_element(*SignUp.CREATE_ACCOUNT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", create_account_button)
        self.driver.execute_script("arguments[0].click();", create_account_button)
        print("create account button clicked and page opened")
        print("open page current url:",self.driver.current_url)
        print("")
        time.sleep(6)
        
        # check message text
        if "Congratulations! Your new account has been successfully created!" in self.driver.page_source:
            print("Sign up completed message found in opened page.\n Sign up completed and page opened")
        else:
            print("Sign up completed message not found in opened page")

        # check current url
        if self.driver.current_url == "https://www.automationexercise.com/account_created":
            print("Sign up completed page opened. checked with current url")
        else:
            print("Sign up completed failed")
        time.sleep(10)    
        print("")
    

    # continue button test 
    def click_continue(self):
        continue_button = self.driver.find_element(*SignUp.CONTINUE)
        self.driver.execute_script("arguments[0].click();", continue_button)
        print("continue button clicked and page opened")
        print("open page current url:",self.driver.current_url)  
        time.sleep(4)
        print("")    

