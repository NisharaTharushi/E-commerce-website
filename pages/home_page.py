from selenium.webdriver.common.by import By
import time

# webdriverwait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home():
    def __init__(self, driver):
        self.driver = driver
        
    # locators
    LOGO = (By.CSS_SELECTOR, "img[alt='Website for automation practice']")  
    HEADER = (By.CSS_SELECTOR, "header")
    SEARCH_FIELD = (By.ID, "search_product")  
    SEARCH_BUTTON = (By.ID,"submit_search")
    WOMEN_PANEL = (By.ID, "Women")
    MEN_PANEL = (By.ID, "Men")
    KIDS_PANEL = (By.ID, "Kids")
    BRANDS_LIST = (By.XPATH, "//div[@class='brands_products']//li/a")


    # home page logo
    print("---- Home page ----")
    def get_logo(self):
        print("Logo:")
        logo = self.driver.find_element(*Home.LOGO)
        print(logo.get_attribute("src"))
        print("")

    # header
    def get_header(self):
        print("Header:")
        header = self.driver.find_element(*Home.HEADER)
        for link in header.find_elements(By.TAG_NAME, "a"):
            print("href: ",link.get_attribute("href"))
            print("text:",link.text)
            print("innerHTML:",link.get_attribute("innerHTML"))
            print("innerText:",link.get_attribute("innerText"))
            print("")
        print("")  


    # search
    def search_field(self, value):
        print("Search field:")
        search_field = self.driver.find_element(*Home.SEARCH_FIELD)
        search_field.send_keys(value)
        print("search field value:",search_field.get_attribute("value"))
        print("")    


        search_button = self.driver.find_element(*Home.SEARCH_BUTTON)
        self.driver.execute_script("arguments[0].click();", search_button)
        print("search button clicked and page opened")
        print("open page current url:",self.driver.current_url)
        time.sleep(2)


    # women categories
    def women_categories(self):
        print("---- Women Subcategories: ----")
        category = self.driver.find_element(*Home.WOMEN_PANEL)
        sub_links = category.find_elements(By.TAG_NAME, "a")
        for link in sub_links: 
            print(link.get_attribute("innerText"))
            print(link.get_attribute("href"))
            print("")
            time.sleep(1)
        print("")

        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(link))
            self.driver.execute_script("arguments[0].click();", link)
            print("Clicked:", link.text)
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
        except Exception as e:
            print(f"Couldn't click '{link.text}': {e}")


    # men categories
    def men_categories(self):
        print("---- Men Subcategories: ----")
        category = self.driver.find_element(*Home.MEN_PANEL)
        sub_links = category.find_elements(By.TAG_NAME, "a")
        for link in sub_links:
            print(link.get_attribute("innerText"))
            print(link.get_attribute("href"))
            print("")
            time.sleep(1)
        print("")
        

    # kids categories
    def kids_categories(self):
        print("---- Kids Subcategories: ----")
        category = self.driver.find_element(*Home.KIDS_PANEL)
        sub_links = category.find_elements(By.TAG_NAME, "a")
        for link in sub_links:
            print(link.get_attribute("innerText"))
            print(link.get_attribute("href"))
            print("")
            time.sleep(1)
        print("")


    # brands test 
    def check_all_brands(self):
        print("Checking all brand links:")
        brand_links = self.driver.find_elements(*Home.BRANDS_LIST)
        
        for i in range(len(brand_links)):
            brand_links = self.driver.find_elements(*Home.BRANDS_LIST)
            link = brand_links[i]
            brand_name = link.text
            print("Brand index:",link.text)
            print(f"Brand Name: {brand_name}")
            print(f"Brand Link: {link.get_attribute('href')}")
            print("")


    # click brands test
    def click_all_brands(self):
            print("Checking all brand links:")
            brand_links = self.driver.find_elements(*Home.BRANDS_LIST)

            for i in range(len(brand_links)):
                brand_links = self.driver.find_elements(*Home.BRANDS_LIST)
                link = brand_links[i]
                brand_name = link.text
                print("Brand index:",link.text)
                print(f"Brand Name: {brand_name}")
                print(f"Brand Link: {link.get_attribute('href')}")
                print("")
                # check if the link is clickable
                try:  
                    # Scroll into view and click
                    self.driver.execute_script("arguments[0].scrollIntoView();", link)
                    self.driver.execute_script("arguments[0].click();", link)
                    print(f"Clicked on brand: {brand_name}")
                    print("clicked om brand value:",brand_name.get_attribute("value"))
                    print("open page current url:",self.driver.current_url)
                    time.sleep(2)
                    print("")

                    # do something on the brand page, e.g., print heading
                    heading = self.driver.find_element(By.TAG_NAME, "h2").text
                    print(f"Brand Page Heading: {heading}")
                    print("open page current url:",self.driver.current_url)
                    print("")
                    time.sleep(1)

                    self.driver.back()
                    time.sleep(2)
                except Exception as e:
                    print(f"Error with brand '{brand_name}': {e}")
                    continue   
                print("\n")
        


        
