
import requests
from bs4 import BeautifulSoup

url = "https://www.feedbooks.com/search?cat=FBFIC016000&query=feedbooks"

response = requests.get(url, headers={"Accept": "text/html"})

parsed_response = BeautifulSoup(response.text, "html.parser")

print(parsed_response.prettify())