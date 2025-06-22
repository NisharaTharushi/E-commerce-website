
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver


from pages.home_page import Home


driver = webdriver.Firefox() 
driver.get("https://www.automationexercise.com/products")
# maximize_window
driver.maximize_window()


home = Home(driver)


home.search_field(
    value="dress"
)
home.get_logo()
home.get_header()
home.women_categories()
home.men_categories()
home.kids_categories()
home.check_all_brands()
home.click_all_brands()

