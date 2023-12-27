# Automated Lottery Data Scraper and Google Sheets Integrator

This README provides detailed instructions and explanations for using the Automated Lottery Data Scraper and Google Sheets Integrator. This Python script is designed to automate the process of scraping lottery results from a specific website and storing the collected data in a Google Sheets document. The script employs several Python libraries and technologies, including Tkinter for user interaction, Selenium for web scraping, gspread for Google Sheets integration, and BeautifulSoup for HTML parsing.

## Features

1. **User-Defined Duration**: Utilizes Tkinter to prompt the user for a scraping frequency (in minutes).
2. **Google Sheets Integration**: Automatically updates a specified Google Sheets document with scraped data.
3. **Headless Browser Automation**: Uses Selenium with Chrome in headless mode for seamless data scraping.
4. **Structured Data Storage**: Organizes scraped data in a user-friendly format in Google Sheets.
5. **Automated Login and Data Extraction**: Logs into the target website and extracts lottery result data at regular intervals.

## Requirements

- Python 3.x
- Selenium
- gspread
- oauth2client
- BeautifulSoup
- ChromeDriver (compatible with the installed version of Chrome)
- A Google Cloud Platform account with Google Sheets API enabled
- A .env file with the path to your Google Sheets credentials JSON file

## Setup and Installation

1. **Environment Setup**: 
   - Install Python 3.x from the official website.
   - Install required Python libraries: `pip install selenium gspread oauth2client beautifulsoup4 python-dotenv`.

2. **ChromeDriver Setup**:
   - Download ChromeDriver from its official website.
   - Ensure it is compatible with your Chrome browser's version.
   - Place the ChromeDriver executable in a known directory.

3. **Google Sheets API Setup**:
   - Go to the Google Cloud Platform Console.
   - Create a new project and enable the Google Sheets API.
   - Create credentials for a service account and download the JSON file.
   - Place this JSON file in a secure location and note its path.

4. **.env File**:
   - Create a `.env` file in the same directory as your script.
   - Add the following line: `GOOGLE_SHEETS_CREDENTIALS_PATH="<path_to_your_service_account_json>"`.

5. **Google Sheets Preparation**:
   - Create a new Google Sheets document.
   - Share it with the email found in your service account JSON file with editor access.

## Usage

1. **Running the Script**:
   - Execute the script using `python <script_name>.py`.
   - Enter the desired duration (in minutes) for data scraping frequency when prompted.

2. **Data Scraping and Upload**:
   - The script logs into the target website using provided credentials.
   - It scrapes the latest lottery data at the specified intervals.
   - The data is then formatted and uploaded to the specified Google Sheets document.

3. **Monitoring and Maintenance**:
   - The script will run indefinitely. Monitor it for any errors or interruptions.
   - To stop the script, simply terminate the Python process.

## Important Notes

- **Credentials Security**: Ensure that your Google Sheets credentials JSON file is stored securely and not exposed.
- **Website Changes**: The script may require updates if there are changes to the website's HTML structure.
- **Error Handling**: Implement error handling for network issues or unexpected website changes to ensure continuous operation.

## Conclusion

This script provides a convenient and automated way to scrape lottery data and store it in Google Sheets. It is important to periodically check the script’s performance and make necessary updates based on website changes or other factors.