from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome options to ignore SSL errors and insecure connections
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--allow-insecure-localhost')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--disable-web-security')

# Initialize Chrome browser
driver = webdriver.Chrome(options=chrome_options)

# Open the Wi-Fi login page
driver.get('http://192.0.2.1/login.html')  # Replace with your actual login IP

# Wait for the page to fully load
time.sleep(2)

# Find the username and password fields
username_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')

# Enter your credentials
username_field.send_keys('shivasai')
password_field.send_keys('Chitti@511')

# Submit the form (usually ENTER works)
password_field.send_keys(Keys.RETURN)

# Wait to complete login
time.sleep(3)

# Check if login succeeded
if "Login Error" in driver.page_source:
    print("Login failed.")
else:
    print("Login successful!")

# Optionally keep the session alive or close
# driver.quit()
