import pandas as pd


def read_movies():
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

    # Select movies and add ratings
    movies = basics[basics["titleType"] == "movie"]
    movies = movies.merge(ratings, on="tconst")

    return movies


def get_top_movies(movies):
    # Select movies with at least 25000 votes
    movies = movies[movies["numVotes"] >= 25000]

    # Sort movies by rating
    movies = movies.sort_values("averageRating", ascending=False)

    # Select top 250 movies
    top250 = movies.head(250).copy()

    return top250


def get_writers(top250):
    # Read writers information
    crew = pd.read_csv(
        "data/title.crew.tsv.gz",
        sep="\t",
        na_values="\\N",
        usecols=["tconst", "writers"]
    )

    # Add writers IDs to movies
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
    def find_writer_names(writer_ids):
        if pd.isna(writer_ids):
            return ""

        writer_list = writer_ids.split(",")

        writer_names = []

        for writer_id in writer_list:
            writer_names.append(name_map.get(writer_id, writer_id))

        return ", ".join(writer_names)

    top250["Writers"] = top250["writers"].apply(find_writer_names)

    return top250


def save_results(top250):
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

    print(result)


def main():
    movies = read_movies()

    top250 = get_top_movies(movies)

    top250 = get_writers(top250)

    save_results(top250)


if __name__ == "__main__":
    main()