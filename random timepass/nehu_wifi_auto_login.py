import sys
import os
import asyncio
import platform
import getpass
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from cryptography.fernet import Fernet
import time

# Function to get the correct path for EdgeDriver when bundled as an executable
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Function to safely get user input
def get_user_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        print("Error: Unable to read input. Please run the executable from a console.")
        sys.exit(1)

# Configure Edge options to ignore SSL errors and insecure connections
edge_options = Options()
edge_options.add_argument('--ignore-certificate-errors')
edge_options.add_argument('--ignore-ssl-errors')
edge_options.add_argument('--allow-insecure-localhost')
edge_options.add_argument('--allow-running-insecure-content')
edge_options.add_argument('--disable-web-security')

# Set file paths
appdata_path = os.path.join(os.getenv("LOCALAPPDATA"), "NEHU_WiFi")
credentials_file = os.path.join(appdata_path, "credentials.enc")
key_file = os.path.join(appdata_path, "key.key")

# Ensure directory exists
os.makedirs(appdata_path, exist_ok=True)

# Generate and save encryption key if it doesn't exist
def ensure_key():
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)

# Load encryption key
def load_key():
    with open(key_file, 'rb') as f:
        return f.read()

# Save encrypted credentials
def save_credentials(username, password):
    key = load_key()
    fernet = Fernet(key)
    data = json.dumps({'username': username, 'password': password}).encode()
    encrypted = fernet.encrypt(data)
    with open(credentials_file, 'wb') as f:
        f.write(encrypted)

# Load and decrypt credentials
def load_credentials():
    if os.path.exists(credentials_file) and os.path.exists(key_file):
        try:
            key = load_key()
            fernet = Fernet(key)
            with open(credentials_file, 'rb') as f:
                decrypted_data = fernet.decrypt(f.read())
                data = json.loads(decrypted_data.decode())
                return data.get('username'), data.get('password')
        except Exception:
            pass
    return None, None

# Setup key and credentials
ensure_key()
username, password = load_credentials()
if not username or not password:
    print("Credentials not found. Please enter them. (They will be saved securely under LOCALAPPDATA)")
    username = get_user_input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    save_credentials(username, password)

# Initialize Edge browser with Service for EdgeDriver
driver_path = resource_path('msedgedriver.exe')
service = Service(executable_path=driver_path)
driver = webdriver.Edge(service=service, options=edge_options)

async def main():
    try:
        # Open the Wi-Fi login page
        driver.get('http://192.0.2.1/login.html')  # Replace with actual login IP

        # Wait for the page to fully load
        await asyncio.sleep(2)

        # Find the username and password fields
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')

        # Enter the credentials
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the form
        password_field.send_keys(Keys.RETURN)

        # Wait to complete login
        await asyncio.sleep(3)

        # Check if login succeeded
        if "Login Error" in driver.page_source:
            print("Login failed.")
        else:
            print("Login successful!")

    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        driver.quit()

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())