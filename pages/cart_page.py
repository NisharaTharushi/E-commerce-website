from selenium.webdriver.common.by import By
import time
# webdriverwait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

class Cart():
    def __init__(self, driver):
        self.driver = driver

    # locators
    CART_PAGE_URL = "https://www.automationexercise.com/view_cart"
    CART_ITEMS = (By.XPATH, "//tr[contains(@id, 'product')]//td")
    REMOVE_PRODUCT = (By.CLASS_NAME, "cart_quantity_delete")
    PROCEED_CHECKOUT = (By.XPATH, "//a[text()='Proceed To Checkout']")
    CONTINUE_SHOPPING = (By.XPATH, "//a[text()='Continue Shopping']")
    CART_EMPTY_TEXT = (By.XPATH, "//*[contains(text(),'Cart is empty')]")
    PRODUCT_IMAGE = (By.CLASS_NAME, "cart_product")
    MODAL_POPUP = (By.ID, "checkoutModal")

    REGISTER_LOGIN_LINK = (By.XPATH, "//a[text()='Register / Login']")
    CONTINUE_WITH_CART_LINK = (By.XPATH, "//button[contains(text(), 'Continue On Cart')]")
    PRODUCT_WRAPPERS = (By.CLASS_NAME, "product-image-wrapper")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[text()='Continue Shopping']")
    REGISTER_LOGIN_LINK = (By.XPATH, "//a[@href='/login']//u[text()='Register / Login']")
    

    print("---- Open Product Page and Add Products to Cart ----")
    
    # open product page 
    def open_products_page(self):
        self.driver.get("https://www.automationexercise.com/products")
        time.sleep(2)

    # add first and unique products to cart
    def add_first_n_unique_products_to_cart(self, n=3):
        print(f"-- Add {n} Unique Products to Cart --")
        wrappers = self.driver.find_elements(*self.PRODUCT_WRAPPERS)
        count = min(n, len(wrappers))

        for i in range(count):
            product = wrappers[i]
            add_button = product.find_element(By.CLASS_NAME, "add-to-cart")

            self.driver.execute_script("arguments[0].scrollIntoView(true);", product)
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", add_button)
            print(f"Added Product #{i+1}")
            time.sleep(2)

            # Close modal
            self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTON).click()
            print("Clicked 'Continue Shopping'\n")
            time.sleep(2)

    
    # open cart page
    def open_cart_page(self):
        print("---- Opening Cart Page ----")
        self.driver.get(Cart.CART_PAGE_URL)
        print("Cart page URL:", self.driver.current_url)
        time.sleep(2)
        print("")

    # cart items display test
    def verify_cart_items_displayed(self):
        print("---- Checking Cart Items ----")
        items = self.driver.find_elements(*Cart.CART_ITEMS)
        if items:
            print("Cart items found:", len(items))
        else:
            print("Cart is empty or items not displayed.")
        print("")

    # remove button test 
    def remove_first_product(self):
        print("---- Removing First Product ----")
        remove_button = self.driver.find_element(*Cart.REMOVE_PRODUCT)
        self.driver.execute_script("arguments[0].click();", remove_button)
        print("Remove button clicked")
        time.sleep(2)
        print("")

    # checkout button test
    def proceed_to_checkout(self):
        print("---- Proceed to Checkout ----")
        checkout_button = self.driver.find_element(*Cart.PROCEED_CHECKOUT)
        self.driver.execute_script("arguments[0].click();", checkout_button)
        print("Clicked on 'Proceed To Checkout'")
        time.sleep(2)
        print("Current URL:", self.driver.current_url)
        print("")

    # modal popup test 
    def check_modal_popup_displayed(self):
        print("---- Checking for Checkout Modal Popup ----")
        try:
            modal = self.driver.find_element(*Cart.MODAL_POPUP)
            if modal.is_displayed():
                print("Modal popup displayed.")
            else:
                print("Modal popup not displayed.")
        except Exception:
            print("Modal popup not found.")
        print("")

    
    # continue with cart icon test 
    def click_continue_with_cart(self):
        print("---- Clicking 'Continue On Cart' ----")
        try:
            # Wait for the modal to be visible
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(Cart.MODAL_POPUP)
            )

            # wait for the 'Continue On Cart' link to be clickable
            continue_link = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(Cart.CONTINUE_WITH_CART_LINK)
            )
            continue_link.click()
            print("Clicked 'Continue On Cart'.")
            print("Navigated to checkout page.")
            time.sleep(2)
            print("Current URL:", self.driver.current_url)

        except TimeoutException:
            print("'Continue with Cart' not found or not clickable — modal may not have appeared.")
        except NoSuchElementException:
            print("Modal or link element not found.")
        print("")

    # product images test 
    def verify_product_images(self):
        print("---- Verifying Product Images ----")
        images = self.driver.find_elements(*Cart.PRODUCT_IMAGE)
        if images:
            print("Product images found:", len(images))
        else:
            print("No product images found.")
        print("")

    # cart empty test 
    def is_cart_empty(self):
        print("---- Checking if Cart is Empty ----")
        empty_message = self.driver.find_elements(*Cart.CART_EMPTY_TEXT)
        if empty_message:
            print("Cart is empty message displayed.")
        else:
            print("Cart has items.")
        print("")

    # register login button test 
    def click_register_login(self, email_input, password_input):
        print("---- Clicking 'Register / Login' ----")
        try:
            # Wait for modal to appear
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(Cart.MODAL_POPUP)
            )

            # Wait for Register/Login link to be clickable and click
            register_link = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(Cart.REGISTER_LOGIN_LINK)
            )
            register_link.click()
            print("Redirected to login/signup page.")
            time.sleep(2)
            print("Current URL:", self.driver.current_url)

            # Fill in login credentials and click login
            email = self.driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
            email.send_keys(email_input)

            password = self.driver.find_element(By.XPATH, "//input[@data-qa='login-password']")
            password.send_keys(password_input)

            self.driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
            print("Login submitted.\n")

        except TimeoutException:
            print("Register/Login link not found or modal didn't appear.")
        print("")
