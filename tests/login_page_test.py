import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.login_page import Login

driver = webdriver.Firefox() 
driver.get("https://www.automationexercise.com/login")

product = Login(driver)

product.login(
    email="tharushinishar129@gmail.com",
    password="373838"
)

