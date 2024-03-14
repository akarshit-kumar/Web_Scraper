import requests
from bs4 import BeautifulSoup

class Evaluator:

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def make_request(self):
        url = "https://food.grab.com/sg/en/"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.RequestException as err:
            print("Request Error:", err)

    def get_h1_tags(self):
        response = self.make_request()
        soup = BeautifulSoup(response.text, 'html.parser')
        h1_tag = soup.find('h1')
        if h1_tag:
            print("This is without HTML tags:", h1_tag.text)
        else:
            print("H1 tag not found")

    def get_title(self):
        response = self.make_request()
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('title')
        if title_tag:
            print("This is the title:", title_tag.text)
        else:
            print("Title tag not found")

    def get_div(self):
        response = self.make_request()
        soup = BeautifulSoup(response.text, 'html.parser')
        div_tag = soup.find('div')
        if div_tag:
            print("The information in all divs:", div_tag.text)
        else:
            print("Div tag not found")

# Create an instance of the Evaluator class
evaluator = Evaluator()

# Call the get_div() method
evaluator.get_div()
