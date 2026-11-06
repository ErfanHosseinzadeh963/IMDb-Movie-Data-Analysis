import pandas as pd

basics = pd.read_csv(
    "data/title.basics.tsv.gz",
    sep="\t",
    na_values="\\N",
    usecols=["tconst", "titleType", "primaryTitle", "startYear", "genres"],
    low_memory=False
)

ratings = pd.read_csv(
    "data/title.ratings.tsv.gz",
    sep="\t",
    na_values="\\N"
)

movies = basics[basics["titleType"] == "movie"]

movies = movies.merge(ratings, on="tconst")

movies = movies[movies["numVotes"] >= 25000]

movies = movies.sort_values("averageRating", ascending=False)

top250 = movies.head(250)

top250.to_csv("data/imdb_top250.csv", index=False)

print(top250)
