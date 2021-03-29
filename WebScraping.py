from bs4 import BeatifulSoup

import requests

site = requests.get("https://www.climatempo.com.br/").content
#objeto site recebe todo conteudo da requisição http do site..
soup = BeatifulSoup(site, 'html.parser')
#objeto soup baixando do site o html
#print(soup.prettify())
#transforma o html em string e o print vai exibir o html

temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

print(temperatura.string)

print(soup.title.string)

print(soup.find('admin'))