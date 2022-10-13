from os import link
from venv import create
import pandas as pd
import pickle
genomeScores = "./pickle/genomeScores.pkl"
genomeTags = "./pickle/genomeTags.pkl"
links = "./pickle/links.pkl"
movies = "./pickle/movies.pkl"
ratings = "./pickle/ratings.pkl"
tags = "./pickle/tags.pkl"
pkls = [    genomeScores,
        genomeTags,
        links,
        movies,
        ratings,
        tags]

def create_pkl(all=False):
    ratings_csv = pd.read_csv("./ml-25m/ratings.csv")
    
    # if you pass True into create_pkl() it will recreate the pickle files for every csv,
    # by default it will only create the ratings csv since that one was too large to add to git and has to be done manually on each persons computer. 
    if all:  
        genomeScores_csv = pd.read_csv("./ml-25m/genome-scores.csv")
        genomeTags_csv = pd.read_csv("./ml-25m/genome-tags.csv")
        links_csv = pd.read_csv("./ml-25m/links.csv")
        movies_csv = pd.read_csv("./ml-25m/movies.csv")
        tags_csv = pd.read_csv("./ml-25m/tags.csv")
        csvs = [    genomeScores_csv,
            genomeTags_csv,
            links_csv,
            movies_csv,
            ratings_csv,
            tags_csv]
        names = ["genomeScores", "genomeTags", "links", "movies", "ratings", "tags"]

        for i in range(len(csvs)):
            csvs[i].to_pickle(f"./pickle/{names[i]}.pkl")
    else:
        ratings_csv.to_pickle("./pickle/ratings.pkl")        


def add_to_pickle(path, item):
    with open(path, 'ab') as file:
        pickle.dump(item, file, pickle.HIGHEST_PROTOCOL)


def read_from_pickle(path):
    with open(path, 'rb') as file:
        try:
            while True:
                yield pickle.load(file)
        except EOFError:
            pass
def main():
    # uncomment this to make the pickle file for ratings
    # make sure to download the zip file from the MovieLens dataset here and unzip it into the ml-25m folder
    # https://grouplens.org/datasets/movielens/25m/
    #create_pkl()
    #for item in read_from_pickle(genomeScores):
    #    repr(item)

    # Counts how many rows have null values in each table
    for file in pkls:
        df = pd.read_pickle(file)
        print(file, len(df[df.isnull().any(axis=1)]))

    return 0



if __name__ == "__main__":
    main()
