import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver


from pages.contact_us_page import ContactUsPage

driver = webdriver.Firefox() 
driver.get("https://www.automationexercise.com/contact_us")
# maximize_window


contact = ContactUsPage(driver)


contact.set_name("Tharushi")
contact.set_email("tharushina@gmail")
contact.set_subject("hello")
contact.set_message("hello")
contact.upload_file_path("C:\\Users\\User\\Desktop\\Nishara QA CV .pdf")
contact.submit_form()

