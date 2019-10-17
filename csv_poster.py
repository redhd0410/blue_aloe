import pandas as pd
import os
import urllib


def image_scrape(posters_df):
    base_url = "http://image.tmdb.org/t/p/w185/"
    posters_count = posters.count()
    # 먼저 directory 안에 posters_data라는 폴더를 만들어 
    os.chdir(os.getcwd() + "/posters_data")
    for i in range(posters_count):
        urllib.request.urlretrieve(base_url + posters_df[i][1:], posters_df[i][1:])


if __name__ == '__main__':
    df = pd.read_csv('movies_metadata.csv')
    posters = df['poster_path']
    image_scrape(posters)
