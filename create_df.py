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


def create_pkl():
    genomeScores_csv = pd.read_csv("./ml-25m/genome-scores.csv")
    genomeTags_csv = pd.read_csv("./ml-25m/genome-tags.csv")
    links_csv = pd.read_csv("./ml-25m/links.csv")
    movies_csv = pd.read_csv("./ml-25m/movies.csv")
    ratings_csv = pd.read_csv("./ml-25m/ratings.csv")
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
    for item in read_from_pickle(genomeScores):
        print(repr(item))

    return 0



if __name__ == "__main__":
    main()
