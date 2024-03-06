import os
import requests
import dotenv
import tkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup
import time
from datetime import datetime

# Function to ask for duration using Tkinter
def ask_duration():
    ROOT = tk.Tk()
    ROOT.withdraw()
    # The input dialog
    USER_INP = simpledialog.askstring(title="Set Duration",
                                      prompt="Enter Duration in Seconds:")
    return int(USER_INP)  # Convert minutes to seconds

def safe_append_to_worksheet(worksheet, data, max_retries=100, delay=5):
    attempts = 0
    while True:
        try:
            worksheet.append_row(data)
            break  # Break the loop if successful
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error occurred: {e}. Retrying...")
            time.sleep(delay)  # Wait for a while before retrying
            attempts += 1
    else:
        print("Failed to append data after several retries.")

# Set duration time
duration = ask_duration()

# Load environment variables from the .env file
dotenv.load_dotenv()

# Load Google Sheets credentials from environment variable
google_credentials_path = os.getenv('GOOGLE_SHEETS_CREDENTIALS_PATH')
if not google_credentials_path:
    raise ValueError("The Google Sheets credentials path is not set in the environment variables")

# Set the scope and credentials for Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(google_credentials_path, scope)
client = gspread.authorize(creds)

# Open the Google Spreadsheet by title
sheet_url = "https://docs.google.com/spreadsheets/d/1uQSwZAYr629_rGdO1F74Y51p3z0DNtBZJC7VbhbNcPs/edit?usp=sharing"
spreadsheet = client.open_by_url(sheet_url)

# Get the worksheet by name
worksheet_name = "Sheet1"
worksheet = spreadsheet.get_worksheet(0)

# If the worksheet is not found, create a new one
if worksheet is None:
    worksheet = spreadsheet.add_worksheet(title=worksheet_name, rows="100", cols="20")

# Define the header names
header_names = ["Data Time", "ยี่กี HUAY 5 นาที", "ยี่กี HUAY VIP 5 นาที", "ยี่กี LTO 5 นาที", "ยี่กี LTO VIP 5 นาที", "ยี่กี ชัดเจน 5 นาที", "ยี่กี ชัดเจน VIP 5 นาที"]
total_data = [header_names]
# Check if the worksheet is empty (no header row) and add headers if needed
existing_headers = worksheet.row_values(1)
if not existing_headers:
    worksheet.insert_row(header_names, index=1)

# Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# URL of the login page
login_url = 'https://lottoone.net/login'

# Your login credentials
username = 'lottoone7124'
password = 'ABCdef123'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(login_url)

# Wait for the page to load
time.sleep(2)

# Find the username and password input fields and the submit button
username_field = driver.find_element(By.ID, 'inputUsername')
password_field = driver.find_element(By.ID, 'inputPassword')
submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

# Enter your login credentials
username_field.send_keys(username)
password_field.send_keys(password)

# Submit the form
submit_button.click()

# Wait for the next page to load or for login to complete
time.sleep(5)

# Repeat the data extraction every 'duration' seconds
while True:
    # Navigate to the data URL
    driver.get("https://lottoone.net/member/lotto/result")
    time.sleep(3)

    # Extract the data
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    div_elements = soup.find_all('div', class_='card card-fulid my-2')

    order = [5, 7, 9, 11, 13, 15]
    data = []
    data_com = []
    current_datetime = datetime.now()
    # Format the date and time as YYYY-MM-DD HH:MM
    data_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    data.append(data_time)
    for item in order:
        # Check if the index 'item' is within the range of 'div_elements'
        if item < len(div_elements):
            div_element = div_elements[item]
            span_element = div_element.find('span', class_='mb-0 mx-auto')
            divs_font_numeral = div_element.find_all('div', class_='font-numeral')

            # Check if the necessary elements are found
            if span_element and len(divs_font_numeral) >= 2:
                value_1 = span_element.get_text().split(" ")[-1]
                value_2 = divs_font_numeral[0].get_text()
                value_3 = divs_font_numeral[1].get_text()

                data.append(value_1)
                data.append(value_2)
                data.append(value_3)
                data_com.append(value_1)
                data_com.append(value_2)
                data_com.append(value_3)
            else:
                print(f"Required elements not found for item at index {item}.")
        else:
            print(f"Index {item} is out of range for 'div_elements'.")
    print(data)
    try:
        if data_com != total_data[-1] and len(data) >= 19:
                total_data.append(data_com)
                if data_com[0] == data_com[3] == data_com[6] == data_com[9] == data_com[12] == data_com[15]:
                    if data_com[0] == "1":
                        if data_com[1] != "XXX" and data_com[4] != "XXX" and data_com[7] != "XXX" and data_com[10] != "XXX" and data_com[13] != "XXX" and data_com[16] != "XXX":

                            safe_append_to_worksheet(worksheet, data)

                            if data_com[0] == data_com[3] == data_com[6] == data_com[9] == data_com[12] == data_com[15]:
                                print("Value1 of lotto are same")
                                time.sleep(150)

                    else:
                        safe_append_to_worksheet(worksheet, data)

                        if data_com[0] == data_com[3] == data_com[6] == data_com[9] == data_com[12] == data_com[15]:
                            print("Value1 of lotto are same")
                            time.sleep(150)
    except Exception as e:
        print(f"An error occurred: {e}")
    # Wait for the specified duration before repeating
    time.sleep(duration)

# Note: This loop will run indefinitely. You need to manually stop it or add a condition to break the loop.
