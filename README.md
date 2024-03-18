# Thai Lottery Result Scraper

## Overview
This Python project is designed to scrape and collect data from the Thai lottery website, specifically targeting various lottery games. It automatically extracts the latest results at specified intervals and stores them in a Google Spreadsheet for easy access and analysis.

## Video Preview

[![Video Preview](https://github.com/DevRex-0201/Project-Images/blob/main/video%20preview/Py-Lottery-Selenium-Scraper.png)](https://brand-car.s3.eu-north-1.amazonaws.com/Four+Seasons/Py-Lottery-Selenium-Scraper.mp4)

## Features
- **Automated Data Scraping:** Extracts lottery results from predefined games on the Thai lottery website.
- **Scheduled Scraping:** Executes data scraping at user-defined intervals.
- **Data Storage:** Stores the scraped data in a Google Spreadsheet.
- **Headless Browser Automation:** Uses Selenium with a headless Chrome browser for scraping.
- **User Authentication:** Automates login process to access restricted data.
- **Error Handling and Retry Mechanism:** Implements a retry mechanism for robust data appending to the worksheet.

## Requirements
- Python 3.x
- Selenium WebDriver
- Google Sheets API
- BeautifulSoup
- Tkinter (for GUI input)
- Chrome browser (for headless execution)

## Installation
1. **Install Dependencies:** Use `pip install -r requirements.txt` to install the necessary Python libraries.
2. **Chrome WebDriver:** Ensure that the Chrome WebDriver is installed and added to the system path.
3. **Google Sheets API Setup:** Follow Google's setup guide to configure access to Google Sheets.
4. **Environment File:** Create a `.env` file with your Google Sheets credentials and other environment variables.

## Usage
1. **Set Duration:** When the script runs, a Tkinter dialog will prompt for the scraping interval in seconds.
2. **Google Sheets Configuration:** Enter the URL of the Google Sheet and the worksheet name where the data will be stored.
3. **Running the Script:** Execute the script via `python main.py`. The script runs indefinitely until manually stopped.

## Data Extraction
The script scrapes the following lottery games:
- ยี่กี HUAY 5 นาที
- ยี่กี HUAY VIP 5 นาที
- ยี่กี LTO 5 นาที
- ยี่กี LTO VIP 5 นาที
- ยี่กี ชัดเจน 5 นาที
- ยี่กี ชัดเจน VIP 5 นาที

## Data Structure
The data is structured with timestamps and game results, saved in rows in the specified Google Sheet.

## Disclaimer
This script is intended for educational purposes only. Ensure compliance with the website's terms of service and relevant laws when scraping data.

## Support
For support, please open an issue on the project's GitHub repository.
