from venv import create
import pandas as pd

def create_pkl():
    genomeScores = pd.read_csv("./ml-25m/genome-scores.csv")
    genomeTags = pd.read_csv("./ml-25m/genome-tags.csv")
    links = pd.read_csv("./ml-25m/links.csv")
    movies = pd.read_csv("./ml-25m/movies.csv")
    ratings = pd.read_csv("./ml-25m/ratings.csv")
    tags = pd.read_csv("./ml-25m/tags.csv")
    csvs = [genomeScores, genomeTags, links, movies, ratings, tags]
    names = ["genomeScores", "genomeTags", "links", "movies", "ratings", "tags"]

    for i in range(len(csvs)):
        csvs[i].to_pickle(f"./pickle/{names[i]}.pkl")
def main():

    return 0



if __name__ == "__main__":
    main()
