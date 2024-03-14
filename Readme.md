# Web Scraper Evaluator

## Overview
This Python script performs web scraping on a specified URL and extracts information from the HTML content. It utilizes the requests library for making HTTP requests and BeautifulSoup for parsing HTML.

## Table of Contents
- [Setup](#setup)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Usage](#usage)
- [Code Explanation](#code-explanation)

## Setup

### Create a Virtual Environment
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the following commands to create a virtual environment:
    ```bash
    # On Windows
    python -m venv venv

    # On macOS and Linux
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

### Install Dependencies
While inside the virtual environment, install the required dependencies:
```bash
pip install requests beautifulsoup4
```
Or simply do command below 
```bash
pip install -r requirements.txt

```
## Usage

#### How to run file
```bash
python3 main.py
```
### Code Explanation
In the constructor (__init__ method), the class initializes a dictionary called headers containing a user-agent string. This user-agent string is designed to mimic a web browser, helping to avoid potential blocking from websites.

The make_request method sends an HTTP GET request to a specified URL, utilizing the headers defined in the constructor. It handles potential HTTP errors and request exceptions, printing corresponding error messages.

The get_h1_tags method retrieves the first 'h1' tag from the HTML content of a web page. If the tag is found, it prints the text content without HTML tags; otherwise, it indicates that the 'h1' tag was not found.

Similarly, the get_title method extracts and prints the text content of the 'title' tag from the web page.

The get_div method focuses on the first 'div' tag in the HTML content and prints its text content. If no 'div' tag is found, a message stating that the 'div' tag was not found is printed.

Finally, an instance of the Evaluator class is created, and the get_div method is called to demonstrate the functionality. This involves making an HTTP request to a specific URL and extracting and printing information from the first 'div' tag of the web page.





