import pandas as pd
import os
import urllib
import boto3
import requests

def image_scrape(posters_df):
    base_url = "http://image.tmdb.org/t/p/w185/"
    posters_count = posters_df.count()
    # 먼저 directory 안에 posters_data라는 폴더를 만들어 주세요! 
    os.chdir(os.getcwd() + "/posters_data")
    for i in range(posters_count):
        poster_url = base_url + posters_df[i][1:]
        print("running...." + poster_url)
        if (len(posters_df[i]) == 32):
            try:
                urllib.request.urlretrieve(poster_url, posters_df[i][1:])
            except requests.exceptions.RequestException as e:
                continue
        elif (os.path.isfile(posters_df[i][1:])):
            print("file is already in the directory.")
            continue
        else:
            continue

if __name__ == '__main__':
    df = pd.read_csv('movies_metadata.csv', keep_default_na = False)
    posters = df["poster_path"]
    posters_count = posters.count()
    image_scrape(posters)
