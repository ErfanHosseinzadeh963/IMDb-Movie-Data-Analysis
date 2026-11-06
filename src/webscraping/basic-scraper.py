import pandas as pd

basics = pd.read_csv("data/title.basics.tsv.gz", sep="\t", na_values="\\N")
ratings = pd.read_csv("data/title.ratings.tsv.gz", sep="\t", na_values="\\N")
crew = pd.read_csv("data/title.crew.tsv.gz", sep="\t", na_values="\\N")
names = pd.read_csv("data/name.basics.tsv.gz", sep="\t", na_values="\\N")

movies = basics[basics["titleType"] == "movie"]

movies = movies.merge(ratings, on="tconst")
movies = movies.merge(crew, on="tconst")

movies = movies[movies["numVotes"] >= 25000]

movies = movies.sort_values("averageRating", ascending=False)

top250 = movies.head(250)

name_map = dict(zip(names["nconst"], names["primaryName"]))

top250["directors"] = top250["directors"].apply(
    lambda x: ", ".join(name_map.get(i, i) for i in str(x).split(","))
)

top250["writers"] = top250["writers"].apply(
    lambda x: ", ".join(name_map.get(i, i) for i in str(x).split(","))
)

result = top250[
    ["primaryTitle", "startYear", "genres",
     "averageRating", "directors", "writers"]
]

result.to_csv("data/imdb_top250.csv", index=False)

print(result)