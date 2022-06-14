from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = ENTER YOUR LINKEDIN EMAIL-ID
ACCOUNT_PASSWORD = ENTER YOUR LINKDEIN PASSWORD
PHONE = ENTER YOUR NUMBER

chrome_driver_path = "C:\Development/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search?keywords=Python%2BDeveloper&location=Bangalore%2BUrban%2C%2BKarnataka%2C%2BIndia&geoId=112376381&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=2627671881&position=1&pageNum=0")

sign_in = driver.find_element_by_class_name("nav__button-secondary")
sign_in.click()

time.sleep(5)

username = driver.find_element_by_id("username")
username.send_keys(ACCOUNT_EMAIL)

password = driver.find_element_by_id("password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        #If application requires phone number and the field is empty, then fill in the number.
        time.sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        #Submit the application
        submit_button = driver.find_element_by_css_selector("footer button")
        submit_button.click()

        if submit_button.get_attribute("data-control-name") =="continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard = driver.find_element_by_class_name("artdeco-modal__confirm-dialog-btn")
            discard.click()
            print("Complex application, Skipped.")
            continue

        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("no application button, skipped")
        continue

time.sleep(5)
driver.quit()

