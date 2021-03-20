from bs4 import BeautifulSoup

import requests 

site = requests.get("https://www.climatempo.com.br/previsao-do-tempo/fim-de-semana/cidade/558/saopaulo-sp").content
soup = BeautifulSoup(site, "html.parser")

#print(soup.prettify())

temperatura = soup.find("p", class_="_margin-t-20 -gray -line-height-20")

print(temperatura.string)
print(soup.title.string)
print(soup.find('admin'))
