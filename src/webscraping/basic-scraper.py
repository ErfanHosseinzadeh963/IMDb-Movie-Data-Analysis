import pandas as pd

# Read movie information
basics = pd.read_csv(
    "data/title.basics.tsv.gz",
    sep="\t",
    na_values="\\N",
    usecols=["tconst", "titleType", "primaryTitle", "startYear", "genres"],
    low_memory=False
)

# Read movie ratings
ratings = pd.read_csv(
    "data/title.ratings.tsv.gz",
    sep="\t",
    na_values="\\N"
)

# Select movies
movies = basics[basics["titleType"] == "movie"]

# Add ratings to movies
movies = movies.merge(ratings, on="tconst")

# Select movies with at least 25000 votes
movies = movies[movies["numVotes"] >= 25000]

# Sort movies by rating
movies = movies.sort_values("averageRating", ascending=False)

# Select top 250 movies
top250 = movies.head(250).copy()

# Read writers information
crew = pd.read_csv(
    "data/title.crew.tsv.gz",
    sep="\t",
    na_values="\\N",
    usecols=["tconst", "writers"]
)

# Add writers IDs
top250 = top250.merge(crew, on="tconst")

# Collect writers IDs
writers_ids = set()

for x in top250["writers"].dropna():
    writers_ids.update(x.split(","))

# Read writers names
names = pd.read_csv(
    "data/name.basics.tsv.gz",
    sep="\t",
    na_values="\\N",
    usecols=["nconst", "primaryName"]
)

# Select only required writers
names = names[names["nconst"].isin(writers_ids)]

# Create dictionary for writers names
name_map = dict(zip(names["nconst"], names["primaryName"]))

# Replace writers IDs with names
top250["Writers"] = top250["writers"].apply(
    lambda x: ", ".join(
        name_map.get(i, i) for i in str(x).split(",")
    )
)

# Select final columns
result = top250[
    [
        "primaryTitle",
        "startYear",
        "genres",
        "averageRating",
        "numVotes",
        "Writers"
    ]
]

# Rename columns
result = result.rename(columns={
    "primaryTitle": "Movie Name",
    "startYear": "Year",
    "genres": "Genre",
    "averageRating": "Rating",
    "numVotes": "Votes"
})

# Save CSV file
result.to_csv("data/imdb_top250.csv", index=False)

# Print result
print(result)
