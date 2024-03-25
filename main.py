from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import time

FILE_NAME = f'Berita_Populer_{datetime.now():%d-%m-%Y}.csv'

def banner():
    print('''
     _   __                     _____                                          
    / | / /__ _      _______   / ___/______________ _____  ____  ___  _____    
   /  |/ / _ \ | /| / / ___/   \__ \/ ___/ ___/ __ `/ __ \/ __ \/ _ \/ ___/    
  / /|  /  __/ |/ |/ (__  )   ___/ / /__/ /  / /_/ / /_/ / /_/ /  __/ /        
 /_/ |_/\___/|__/|__/____/   /____/\___/_/   \__,_/ .___/ .___/\___/_/         
 Author  : Mohammad Husni Mubaraq                /_/   /_/ 
 Version : 1.1                          
          ''')

def detik_hot_news():
    URL = 'https://www.detik.com/terpopuler'
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, 'html.parser')
    list_news = soup.find_all('article', class_='list-content__item')
    for news_list in list_news:
        news_title = news_list.find('h3', class_='media__title').text.strip()
        news_date = news_list.find('div', class_='media__date').text.strip()
        news_link = news_list.find('a', href=True)
        with open(FILE_NAME,'a', newline='') as csv_file:
            writer = csv.writer(csv_file,delimiter=';')
            writer.writerow([news_title,news_date,news_link['href']])

def kumparan_trending():
    BASE_URL = 'https://kumparan.com'
    URL_POINT = '/trending'
    browser_header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'}
    req = requests.get(BASE_URL+URL_POINT, headers=browser_header)
    soup = BeautifulSoup(req.text, 'html.parser')
    news_list = soup.find_all('div', class_='sc-5mlv5q-0 duWSXf')
    for news in news_list:
        news_link = news.find('a',href=True)
        news_title = getattr(news.find('span', {'data-qa-id' :'title'}),'text', None)
        #news_time = getattr(news.find('div',class_='Textweb__StyledText-sc-1ed9ao-0 dGEwVr  c275a64364 txacenter txfdefault txwregular txmicro'),'text',None)
        with open(FILE_NAME,'a', newline='') as csv_file:
            writer = csv.writer(csv_file,delimiter=';')
            writer.writerow([news_title,'undefined',BASE_URL+news_link['href']])

def tempo_trending():
    URL = 'https://www.tempo.co/terpopuler'
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, 'html.parser')
    news_list = soup.find_all('div', class_='card-box ft240 margin-bottom-sm')
    for lists in news_list:
        news_link = lists.find('a', href=True)
        news_title = lists.find('h2', class_ = 'title').text.strip()
        news_time = lists.find('h4', class_= 'date').text.strip()
        with open(FILE_NAME,'a', newline='') as csv_file:
            writer = csv.writer(csv_file,delimiter=';')
            writer.writerow([news_title,news_time,news_link['href']])

def kompas_trending():
    URL = 'https://indeks.kompas.com/terpopuler'
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, 'html.parser')
    news_list = soup.find_all('div', class_='articleItem')
    for lists in news_list:
        news_link = lists.find('a', href=True)
        news_title = lists.find('h2', class_ = 'articleTitle').text.strip()
        news_time = lists.find('div', class_= 'articlePost-date').text.strip()
        with open(FILE_NAME,'a', newline='') as csv_file:
            writer = csv.writer(csv_file,delimiter=';')
            writer.writerow([news_title,news_time,news_link['href']])

def antara_trending():
    URL = 'https://www.antaranews.com/terpopuler'
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, 'html.parser')
    news_list = soup.find_all('div', class_='card__post card__post-list card__post__transition mt-30')
    for lists in news_list:
        news_link = lists.find('a', href=True)
        news_title = lists.find('h2', class_ = 'post_title post_title_medium').text.strip()
        news_time = lists.find('ul', class_= 'list-inline').text.strip()
        with open(FILE_NAME,'a', newline='') as csv_file:
            writer = csv.writer(csv_file,delimiter=';')
            writer.writerow([news_title,news_time,news_link['href']])
    
        
def main():
    banner()
    time.sleep(1)
    print('Preparing...Please Wait..')
    time.sleep(3)
    print('Scrapping Detik...')
    detik_hot_news()
    time.sleep(1)
    print('Scrapping Kumparan...')
    kumparan_trending()
    time.sleep(1)
    print('Scrapping Tempo...')
    tempo_trending()
    time.sleep(1)
    print('Scrapping Kompas...')
    kompas_trending()
    time.sleep(1)
    print('Scrapping AntaraNews...')
    antara_trending()
    print('Selesai Scrapping.')
    time.sleep(3)

if __name__ == '__main__':
    main()