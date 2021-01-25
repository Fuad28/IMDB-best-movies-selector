import requests
from bs4 import BeautifulSoup
import random

url= 'https://www.imdb.com/chart/top'

def main():
    response= requests.get(url).text
    soup= BeautifulSoup(response, 'html.parser')
    tags= soup.select('td.titleColumn')
    year= [x.text.split()[-1] for x in tags]
    actors_list= [x.a['title'] for x in tags]
    movie_names= [x.a.text for x in tags]
    ratings= [float(x['data-value']) for x in soup.select('td.posterColumn span[name= ir]')]
    n_movies= len(movie_names)

    while True:
        idx= random.randrange(0, n_movies)
        print(f'{movie_names[idx]} {year[idx]}, rating: {ratings[idx]:.1f}, starring: {actors_list[idx]} ')

        ask= input('\nDo you want another movie (y/[n])? ')
        if ask.lower() != 'y':
            break
if __name__ == '__main__':
    main()