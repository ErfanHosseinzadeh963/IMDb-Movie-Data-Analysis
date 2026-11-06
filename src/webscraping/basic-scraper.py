from pathlib import Path

import pandas as pd


# Project paths
DATA_DIR = Path("data")

BASICS_FILE = DATA_DIR / "title.basics.tsv.gz"
RATINGS_FILE = DATA_DIR / "title.ratings.tsv.gz"
CREW_FILE = DATA_DIR / "title.crew.tsv.gz"
NAMES_FILE = DATA_DIR / "name.basics.tsv.gz"

OUTPUT_FILE = DATA_DIR / "imdb_top250.csv"

MIN_VOTES = 25000
TOP_MOVIES_COUNT = 250


def load_data():
    """Load movie information and ratings."""

    basics = pd.read_csv(
        BASICS_FILE,
        sep="\t",
        na_values="\\N",
        usecols=[
            "tconst",
            "titleType",
            "primaryTitle",
            "startYear",
            "genres"
        ],
        low_memory=False
    )

    ratings = pd.read_csv(
        RATINGS_FILE,
        sep="\t",
        na_values="\\N"
    )

    return basics, ratings


def get_top_movies(basics, ratings):
    """Select the top 250 movies based on ratings and votes."""

    movies = basics[basics["titleType"] == "movie"]

    movies = movies.merge(
        ratings,
        on="tconst"
    )

    movies = movies[movies["numVotes"] >= MIN_VOTES]

    movies = movies.sort_values(
        by="averageRating",
        ascending=False
    )

    return movies.head(TOP_MOVIES_COUNT).copy()


def load_writer_names(top_movies):
    """Find writer names for selected movies."""

    crew = pd.read_csv(
        CREW_FILE,
        sep="\t",
        na_values="\\N",
        usecols=["tconst", "writers"]
    )

    top_movies = top_movies.merge(
        crew,
        on="tconst",
        how="left"
    )

    writer_ids = set()

    for writers in top_movies["writers"].dropna():
        writer_ids.update(writers.split(","))

    names = pd.read_csv(
        NAMES_FILE,
        sep="\t",
        na_values="\\N",
        usecols=["nconst", "primaryName"]
    )

    names = names[names["nconst"].isin(writer_ids)]

    name_map = dict(
        zip(names["nconst"], names["primaryName"])
    )

    def get_names(writer_ids):
        if pd.isna(writer_ids):
            return ""

        return ", ".join(
            name_map.get(writer_id, writer_id)
            for writer_id in writer_ids.split(",")
        )

    top_movies["Writers"] = top_movies["writers"].apply(get_names)

    return top_movies


def prepare_output(top_movies):
    """Prepare the final dataset."""

    result = top_movies[
        [
            "primaryTitle",
            "startYear",
            "genres",
            "averageRating",
            "numVotes",
            "Writers"
        ]
    ].copy()

    result = result.rename(columns={
        "primaryTitle": "Movie Name",
        "startYear": "Year",
        "genres": "Genre",
        "averageRating": "Rating",
        "numVotes": "Votes"
    })

    return result


def save_results(data):
    """Save the final dataset as a CSV file."""

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    data.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(f"Data saved successfully: {OUTPUT_FILE}")


def main():
    """Run the IMDb scraping project."""

    basics, ratings = load_data()

    top_movies = get_top_movies(basics, ratings)

    top_movies = load_writer_names(top_movies)

    result = prepare_output(top_movies)

    save_results(result)


if __name__ == "__main__":
    main()
