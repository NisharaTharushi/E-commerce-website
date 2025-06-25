import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.products_page import ProductsPage

driver = webdriver.Firefox() 
driver.get("https://www.automationexercise.com/products")
# maximize_window
driver.maximize_window()

product = ProductsPage(driver)

product.get_logo()
product.get_header()
product.women_categories()
product.men_categories()
product.kids_categories()
product.view_product_buttons()
product.product_cards() 
product.add_to_cart_buttons()

