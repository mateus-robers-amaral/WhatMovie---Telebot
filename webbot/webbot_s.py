from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import re

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('window-size=800,800')

chrome_driver = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service = chrome_driver, options = chrome_options)

urls = ['https://www.rottentomatoes.com/browse/movies_at_home/genres:action~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:adventure~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:animation~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:anime~sort:popular?page=2',
         'https://www.rottentomatoes.com/browse/movies_at_home/genres:biography~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:comedy~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:crime~sort:popular?page=2',
         'https://www.rottentomatoes.com/browse/movies_at_home/genres:documentary~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:drama~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:entertainment~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:faith & spirituality~sort:popular?page=2',
         'https://www.rottentomatoes.com/browse/movies_at_home/genres:fantasy~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:game show~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:lgbtq+~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:health & wellness~sort:popular?page=2',
           'https://www.rottentomatoes.com/browse/movies_at_home/genres:history~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:holiday~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:horror~sort:popular?page=2',
         'https://www.rottentomatoes.com/browse/movies_at_home/genres:house & garden~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:kids & family~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:music~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:musical~sort:popular?page=2', 
         'https://www.rottentomatoes.com/browse/movies_at_home/genres:mystery & thriller~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:nature~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:news~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:reality~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:romance~sort:popular?page=2',
           'https://www.rottentomatoes.com/browse/movies_at_home/genres:sci-fi~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:short~sort:popular?page=2',
           'https://www.rottentomatoes.com/browse/movies_at_home/genres:soap~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:special interest~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:sports~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:stand-up~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:talk show~sort:popular?page=2',
             'https://www.rottentomatoes.com/browse/movies_at_home/genres:travel~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:variety~sort:popular?page=2',
           'https://www.rottentomatoes.com/browse/movies_at_home/genres:war~sort:popular?page=2', 'https://www.rottentomatoes.com/browse/movies_at_home/genres:western~sort:popular?page=2']

with open('filmes.csv', 'w', encoding='utf-8') as file:
            file.write('FILM, POSTING, CRITIC, AUDIENCE, GENRE \n')
for url in urls:
    driver.get(url)
    time.sleep(2)

    film_titles = driver.find_elements(By.CLASS_NAME, 'p--small')
    film_posts = driver.find_elements(By.CLASS_NAME, 'smaller')
    film_scores = driver.find_elements(By.TAG_NAME, 'score-pairs-deprecated')

    films_title = []
    films_post = []
    films_critic = []
    films_audience =[]


    for film in film_titles[4:]:
        films_title.append(film.text)

    for date in film_posts:
        films_post.append(date.text.replace(',', '|'))

    for score in film_scores:
        per = score.text.split('\n')
        films_critic.append(per[0])
        films_audience.append(per[1])

    genre = re.search(r'genres:(\w+)', url)
    list_films = []
    n = 0
    for i, e in enumerate(films_title):
        list_films.append(f'{films_title[n]}, {films_post[n]}, {films_critic[n]}, {films_audience[n]}, {genre.group(1)}')
        n += 1
        if n == 10:
            break

    with open('filmes.csv', 'a', encoding='utf-8') as file:
                for film in list_films:
                    file.write(film + '\n')
driver.quit()


#TRATAR OS DADOS E COLOCAR SO O NOME DOS FILMES NO CSV

import pandas as pd

df = pd.read_csv('filmes.csv')
df = df['FILM']
df.to_csv('filmes.csv', index=False)
print(df)