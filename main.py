from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ACCOUNT_EMAIL = "YOUR EMAIL"
ACCOUNT_PASSWORD = "YOUR PASSWORD"
PHONE = "YOUR NUMBER"

chrome_driver_path = "/home/walttersly/Documents/chromedriver_linux64/chromedriver"

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service= service)
# driver.get("https://www.linkedin.com/")

urls = ["https://www.linkedin.com/jobs/search/?currentJobId=3450137584&f_AL=true&keywords=python%20developer&refresh=true&sortBy=R",
        "https://www.linkedin.com/jobs/search/?currentJobId=3365861285&f_AL=true&geoId=100710459&keywords=javascript%20developer&location=Kenya&refresh=true&sortBy=R",
        "https://www.linkedin.com/jobs/search/?currentJobId=3365861285&f_AL=true&geoId=100710459&keywords=react%20developer&location=Kenya&refresh=true&sortBy=R",
        "https://www.linkedin.com/jobs/search/?currentJobId=3446637802&f_AL=true&geoId=100710459&keywords=web%20developer&location=Kenya&refresh=true&sortBy=R",
        "https://www.linkedin.com/jobs/search/?currentJobId=3446637802&f_AL=true&geoId=100710459&keywords=data%20scientist&location=Kenya&refresh=true&sortBy=R"
    ]

# for url in range(len(urls)):
#     driver.get(urls[url])
#     time.sleep(120)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3476232599&f_AL=true&geoId=100710459&keywords=database&location=Kenya&refresh=true")


sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(10)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# time.sleep(25)

# jobs_panel = driver.find_element(By.XPATH, '/html/body/div[5]/header/div/nav/ul/li[3]/a')
# jobs_panel.click()

time.sleep(5)

# search_panel = driver.find_element(By.XPATH, '/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[2]')
# search_input = input("Enter a job you are searching for: ")
# search_panel = driver.find_element(By.CSS_SELECTOR, "input.jobs-search-box__text-input")
# search_panel.send_keys(search_input)
# search_panel.send_keys("Kenya")
# search_panel.send_keys(Keys.ENTER)
# wait = WebDriverWait(driver, 12)
# all_listings = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container--clickable")))
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

time.sleep(5)




for listing in all_listings:
    print(listing)
    listing.click()
    time.sleep(5)

    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)
        
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)

driver.close()