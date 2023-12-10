from bs4 import BeautifulSoup
import requests
import lxml

html_text = requests.get('https://tikisgeckos.com/collections/crested-geckos-1').text
soup = BeautifulSoup(html_text, 'html.parser')
geckos = soup.find_all('div', class_ = 'grid__item small--one-half medium-up--one-fifth')
for index, gecko in enumerate(geckos):
    gecko_name = gecko.find('div', class_ = 'product-card__name').text.replace(' ','').replace('\n','')
    gecko_price = gecko.find('div', class_ = 'product-card__price').text.replace(' ','').replace('\n','')
    with open(f'posts/{index}.txt', 'w') as f:
        f.write(f"Gecko Name: {gecko_name.strip()}\n")
        f.write(f"Gecko Price: {gecko_price.strip()}")
    print(f'File saved: {index}')

