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

print("Population: " + str(population()))

"""
Keeping the below code because it was a pain to write and we may still use it, 
but probably not tbh.

def food_waste():
    url = "https://www.feedingamerica.org/our-work/our-approach/reduce-food-waste"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    
    waste = doc.find_all("strong")[0].text[1:4]
    
    return waste

def Co2():
    url = "https://www.epa.gov/ghgemissions/inventory-us-greenhouse-gas-emissions-and-sinks"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")[6].find("li")
    
    co2 = doc.find_all("ul")
    
    return co2 


print("Food Waste: " + str(food_waste()) + " Billion Pounds")
print("Co2 Emissions: " + str(Co2()))
"""
