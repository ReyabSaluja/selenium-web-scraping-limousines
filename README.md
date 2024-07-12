# Web Scraping Limousine Companies using Selenium

This repository contains a Python script that utilizes Selenium to scrape limousine names from a limousine company directory. The script scrolls through the webpage, loads all the elements, and extracts the limousine names.

## Features

- **Selenium WebDriver**: Uses Selenium WebDriver to automate browser interactions.
- **Scroll Function**: Scrolls through the page to load all limousine entries.
- **Element Extraction**: Extracts limousine names from the page.
- **Error Handling**: Handles scenarios where the "load more" button is not available.

## Prerequisites

- Python 3.x
- Selenium package
- ChromeDriver (Ensure the path to ChromeDriver is correct)

## Usage

### Installing Dependencies

Ensure you have Selenium installed. You can install it using pip:

```bash
pip install selenium
