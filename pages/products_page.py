from selenium.webdriver.common.by import By
import time

class ProductsPage():
    def __init__(self, driver):
        self.driver = driver


    LOGO = (By.CSS_SELECTOR, "img[alt='Website for automation practice']")  
    HEADER = (By.CSS_SELECTOR, "header")
    SEARCH_FIELD = (By.ID, "search_product")  
    SEARCH_BUTTON = (By.ID,"submit_search")
    WOMEN_PANEL = (By.ID, "Women")
    MEN_PANEL = (By.ID, "Men")
    KIDS_PANEL = (By.ID, "Kids")
    BRANDS_LIST = (By.XPATH, "//div[@class='brands_products']//li/a")

    PRODUCT_CARDS = (By.ID, "cartModal")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//a[contains(@class, 'add-to-cart')]")
    CONTINUE_SHOPPING = (By.XPATH, "//button[contains(text(), 'Continue Shopping')]")
    VIEW_PRODUCT_LINKS = (By.XPATH, "//a[contains(text(),'View Product')]")


    print("---- Product page ----")
    def product_cards(self):
        print("-- Product cards --")
        product_cards = self.driver.find_element(*ProductsPage.PRODUCT_CARDS)
        product_cards = product_cards.find_elements(By.CLASS_NAME, "product-image-wrapper")
        for card in product_cards:
            print(card.text)
            print(card.get_attribute("innerText"))
            print(card.get_attribute("innerHTML"))
            print("")


        print("---- h2 tags in product cards ----")
        product_cards = self.driver.find_element(*ProductsPage.PRODUCT_CARDS)
        product_cards = product_cards.find_elements(By.TAG_NAME, "h2")
        for card in product_cards:
            print("h2 tags:",card.text)
            print("h2 tags innerHTML:",card.get_attribute("innerHTML"))
            print("h2 tags innerText:",card.get_attribute("innerText"))
        print("")
        

        print("p tags in product cards:")
        product_cards = self.driver.find_element(*ProductsPage.PRODUCT_CARDS)
        product_cards = product_cards.find_elements(By.TAG_NAME, "p")
        for card in product_cards:
            print("p tags:",card.text)
            print("p tags innerText:",card.get_attribute("innerText"))
            print("p tags innerHTML:",card.get_attribute("innerHTML"))
        print("")


        print("a tags in product cards:")
        product_cards = self.driver.find_element(*ProductsPage.PRODUCT_CARDS)
        product_cards = product_cards.find_elements(By.TAG_NAME, "a")
        for card in product_cards:
            print("a tags:",card.text)
            print("a tags innerHTML:",card.get_attribute("innerHTML"))
            print("a tags href:",card.get_attribute("href"))
            print("a tags innerText:",card.get_attribute("innerText"))
            print("")


    def add_to_cart_buttons(self):
        print("---- Add to cart buttons ----")
        buttons = self.driver.find_elements(*ProductsPage.ADD_TO_CART_BUTTONS)
        for button in buttons:
            self.driver.execute_script("arguments[0].click();", button)
            print("Clicked:", button.get_attribute("data-product-id"))
            time.sleep(4)
            self.driver.find_element(*ProductsPage.CONTINUE_SHOPPING).click()
            time.sleep(3)
            print("Button innerHTML:",button.get_attribute("innerHTML"))
        print("Done clicking all 'Add to cart' buttons.\n")

    

    def view_product_buttons(self):
        print("---- View Product buttons ----")
        view_product_buttons = self.driver.find_elements(*ProductsPage.VIEW_PRODUCT_LINKS)
            

        for i in range(len(view_product_buttons)):
            try:
                # Re-fetch the element before clicking to avoid stale references
                buttons = self.driver.find_elements(*ProductsPage.VIEW_PRODUCT_LINKS)
                button = buttons[i]

                self.driver.execute_script("arguments[0].scrollIntoView();", button)
                self.driver.execute_script("arguments[0].click();", button)
                print(f"Clicked 'View Product' button {i + 1}")

                time.sleep(2)

                # Print h2 elements
                print("H2 elements on the product page:")
                h2_elements = self.driver.find_elements(By.TAG_NAME, "h2")
                for h2 in h2_elements:
                    text = h2.text.strip()
                    if text:
                        print("-", text)

                # Print paragraph elements
                print("Paragraphs on the product page:")
                p_elements = self.driver.find_elements(By.TAG_NAME, "p")
                for p in p_elements:
                    text = p.text.strip()
                    if text:
                        print("-", text)
                print("")

                self.driver.back()
                time.sleep(2)

            except Exception as e:
                print(f"Error on button {i + 1}: {e}")


    def get_logo(self):
        print("---- Logo ----")
        logo = self.driver.find_element(*ProductsPage.LOGO)
        print(logo.get_attribute("src"))
        print("")


    def get_header(self):
        print("---- Header ----")
        header = self.driver.find_element(*ProductsPage.HEADER)
        for link in header.find_elements(By.TAG_NAME, "a"):
            print("text:",link.text)
            print("innerText:",link.get_attribute("innerText"))
            print("href: ",link.get_attribute("href"))
            print("innerHTML:",link.get_attribute("innerHTML"))
            print("")
        print("")



    def women_categories(self):
        print("---- Women Subcategories ----")
        category = self.driver.find_element(*ProductsPage.WOMEN_PANEL)
        sub_links = category.find_elements(By.TAG_NAME, "a")
        for link in sub_links: 
            print(link.get_attribute("innerText"))
            print(link.get_attribute("href"))
            print("")
            time.sleep(1)
        print("")

    def men_categories(self):
        print("---- Men Subcategories ----")
        category = self.driver.find_element(*ProductsPage.MEN_PANEL)
        sub_links = category.find_elements(By.TAG_NAME, "a")
        for link in sub_links:
            print(link.get_attribute("innerText"))
            print(link.get_attribute("href"))
            print("")
            time.sleep(1)
        print("")

    def kids_categories(self):
        print("---- Kids Subcategories ----")
        category = self.driver.find_element(*ProductsPage.KIDS_PANEL)
        sub_links = category.find_elements(By.TAG_NAME, "a")
        for link in sub_links:
            print(link.get_attribute("innerText"))
            print(link.get_attribute("href"))
            print("")
            time.sleep(1)
        print("")        