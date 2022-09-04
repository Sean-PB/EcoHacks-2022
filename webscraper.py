import requests
from bs4 import BeautifulSoup

def population():
    url = "https://www.worldometers.info/world-population/us-population/"
    page = requests.get(url)
    doc = BeautifulSoup(page.text, "html.parser")
    
    location = doc.find_all(text=" is ")
    parent = location[0].parent
    pop_number = parent.find_all("strong")[1].string

    return pop_number

print(population())