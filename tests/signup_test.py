import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.signup_page  import SignUp

driver = webdriver.Firefox() 
driver.get("https://www.automationexercise.com/login")

product = SignUp(driver)

product.sign_up(
    name="Tharushi",
    email="tharushinishar12@gmail.com",
    password="373838",
    day="2",
    month="3",
    year="1999",
    full_name="Nishara Tharushi",
    last_name="Nishara",
    company_name="my company",
    address1="No 08",
    address2="kithulewela temple road",
    country_name="Australia",
    state="matara",
    city_name="Matara",
    zipcode="81000",
    mobile_number="0702242491"
)
product.click_continue()



