import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.cart_page  import Cart

driver = webdriver.Firefox() 

product = Cart(driver)

product.open_products_page()
product.add_first_n_unique_products_to_cart()
product.open_cart_page()
product.verify_product_images()
product.verify_cart_items_displayed()
product.remove_first_product()
product.proceed_to_checkout()
product.check_modal_popup_displayed()
product.click_continue_with_cart()
product.proceed_to_checkout()
product.click_register_login("tharushinishar129@gmail.com","373838")
product.is_cart_empty()