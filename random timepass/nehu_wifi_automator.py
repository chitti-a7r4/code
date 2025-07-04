from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup the webdriver (make sure chromedriver is in PATH)
driver = webdriver.Chrome()

# Open the login page
driver.get('https://192.0.2.1/login.html?redirect=edge-http.microsoft.com/captiveportal/generate_204')

# Fill the username and password
username_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')

username_field.send_keys('shivasai')
password_field.send_keys('Chitti@511')

# Submit the form using ENTER key or by clicking the button
password_field.send_keys(Keys.RETURN)

# Optional: Wait to see if the login is successful
time.sleep(3)

# Check if login was successful
if "Login Error" in driver.page_source:
    print("Login failed.")
else:
    print("Login successful!")

# Optionally keep the session or close the browser
# driver.quit()
