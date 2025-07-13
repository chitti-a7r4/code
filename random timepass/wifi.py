import sys
import os
import asyncio
import platform
import getpass
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Function to get the correct path for ChromeDriver when bundled as an executable
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Function to load credentials from a file
def load_credentials():
    try:
        with open('credentials.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

# Function to save credentials to a file
def save_credentials(username, password):
    credentials = {'username': username, 'password': password}
    with open('credentials.json', 'w') as file:
        json.dump(credentials, file)

# Configure Chrome options to ignore SSL errors and insecure connections
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--allow-insecure-localhost')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--disable-web-security')

# Try to load credentials from file
creds = load_credentials()
if creds:
    username = creds['username']
    password = creds['password']
    print("Loaded saved credentials.")
else:
    # Prompt user for credentials
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    # Save credentials to file
    save_credentials(username, password)
    print("Credentials saved.")

# Initialize Chrome browser with ChromeDriver
driver_path = resource_path('chromedriver.exe')
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

async def main():
    # Open the Wi-Fi login page
    driver.get('http://192.0.2.1/login.html')  # Replace with your actual login IP

    # Wait for the page to fully load
    await asyncio.sleep(2)

    # Find the username and password fields
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')

    # Enter the credentials
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the form (usually ENTER works)
    password_field.send_keys(Keys.RETURN)

    # Wait to complete login
    await asyncio.sleep(3)

    # Check if login succeeded
    if "Login Error" in driver.page_source:
        print("Login failed.")
    else:
        print("Login successful!")

    # Close the browser
    driver.quit()

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())