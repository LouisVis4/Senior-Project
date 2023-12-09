from bs4 import BeautifulSoup
import requests
import lxml

html_text = requests.get('https://tikisgeckos.com/collections/crested-geckos-1').text
soup = BeautifulSoup(html_text, 'html.parser')
geckos = soup.find_all('div', class_ = 'grid__item small--one-half medium-up--one-fifth')
for gecko in geckos:
    gecko_name = gecko.find('div', class_ = 'product-card__name').text.replace(' ','').replace('\n','')
    gecko_price = gecko.find('div', class_ = 'product-card__price').text.replace(' ','').replace('\n','')
    print(gecko_name)
    print(gecko_price)
