# 🎬 IMDb Movie Data Analysis

### Discover the World's Highest-Rated Movies Through Data

A Python-based data analysis project that uses IMDb's official non-commercial datasets to identify and explore 250 highly rated movies. The project processes movie information, ratings, genres, release years, and writer details to generate a clean and structured dataset for further analysis.

---

## Project Overview

Movies are more than entertainment — they are data.

This project uses IMDb's publicly available datasets to identify 250 highly rated movies based on their average ratings and number of user votes.

Using Python and Pandas, raw IMDb data is processed, filtered, merged, and transformed into an organized CSV file ready for analysis.

> **Note:** This project generates an independent ranking based on IMDb's public datasets. It does not reproduce IMDb's official Top 250 ranking algorithm.

---

## Key Features

- 🎥 **Movie Selection:** Identifies 250 highly rated movies.
- ⭐ **Rating Analysis:** Uses average ratings and vote counts.
- 📅 **Release Information:** Extracts movie release years.
- 🎭 **Genre Exploration:** Collects movie genres.
- ✍️ **Writer Information:** Matches writer IDs with their names.
- 📊 **CSV Export:** Saves the final dataset in an easy-to-use CSV format.
- ⚡ **Memory-Efficient Processing:** Uses chunk-based reading for large IMDb datasets.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11 | Main programming language |
| Pandas | Data processing and analysis |
| Requests | HTTP requests |
| BeautifulSoup | HTML parsing |
| Poetry | Dependency management |
| Git & GitHub | Version control |

---

## Project Structure

```text
IMDb-Movie-Data-Analysis/
│
├── data/
│   └── imdb_top250.csv
│
├── src/
│   └── webscraping/
│       ├── __init__.py
│       └── basic-scraper.py
│
├── tests/
│   └── __init__.py
│
├── web/
│   ├── src/
│   ├── tests/
│   └── README.md
│
├── .gitignore
├── README.md
├── pyproject.toml
└── poetry.lock
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ErfanHosseinzadeh963/IMDb-Movie-Data-Analysis.git
```

### 2. Navigate to the Project Directory

```bash
cd IMDb-Movie-Data-Analysis
```

### 3. Install Dependencies

Make sure Python 3.11 and Poetry are installed.

```bash
poetry install
```

### 4. Download IMDb Datasets

Download the following official IMDb datasets:

- [title.basics.tsv.gz](https://datasets.imdbws.com/title.basics.tsv.gz)
- [title.ratings.tsv.gz](https://datasets.imdbws.com/title.ratings.tsv.gz)
- [title.crew.tsv.gz](https://datasets.imdbws.com/title.crew.tsv.gz)
- [name.basics.tsv.gz](https://datasets.imdbws.com/name.basics.tsv.gz)

Place all four downloaded files inside the `data/` directory.

### 5. Run the Project

```bash
poetry run python src/webscraping/basic-scraper.py
```

After successful execution, the processed dataset will be saved as:

```text
data/imdb_top250.csv
```

---

## Output Dataset

The generated CSV file contains the following columns:

| Column | Description |
|---|---|
| Rank | Position in the generated ranking |
| Movie Name | Primary movie title |
| Year | Release year |
| Genre | Movie genres |
| Rating | Average IMDb rating |
| Votes | Number of user votes |
| Writers | Names of the movie writers |

The selection criteria include:

- Movie type: `movie`
- Minimum votes: 25,000
- Number of selected movies: 250
- Sorting: Average rating (descending), then vote count (descending)

---

## Data Source

This project uses IMDb's official non-commercial datasets.

🔗 [IMDb Non-Commercial Datasets](https://developer.imdb.com/non-commercial-datasets/)

The datasets are updated regularly by IMDb. Therefore, results may change depending on the dataset version used.

---

## Important Notice

This project is intended for educational and non-commercial purposes.

IMDb datasets are subject to IMDb's applicable terms and conditions. Please review their licensing and usage restrictions before using the data.

---

## Author

**Erfan Hosseinzadeh**

GitHub: [@ErfanHosseinzadeh963](https://github.com/ErfanHosseinzadeh963)

---

### ⭐ If you find this project interesting, feel free to explore the repository!
