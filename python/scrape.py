from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://tikisgeckos.com/collections/crested-geckos-1').text
soup = BeautifulSoup(html_text, 'lmxl')