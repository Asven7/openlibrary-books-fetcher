import csv
from typing import List, Dict

import requests


API_URL = "https://openlibrary.org/search.json"
QUERY = "python"
MAX_BOOKS = 50
YEAR_LIMIT = 2000
OUTPUT_FILE = "books_after_2000.csv"


def fetch_books() -> List[Dict]:
    """Fetch raw book data from Open Library API."""
    params = {
        "q": QUERY,
        "limit": 100,
    }
    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json().get("docs", [])


def filter_books(books: List[Dict]) -> List[Dict]:
    """Filter books published after YEAR_LIMIT."""
    filtered_books = []

    for book in books:
        publish_year = book.get("first_publish_year")

        if publish_year and publish_year > YEAR_LIMIT:
            filtered_books.append(
                {
                    "title": book.get("title", "N/A"),
                    "author": ", ".join(book.get("author_name", ["N/A"])),
                    "first_publish_year": publish_year,
                    "edition_count": book.get("edition_count", 0),
                }
            )

        if len(filtered_books) >= MAX_BOOKS:
            break
        
    filtered_books.sort(key=lambda x: x["first_publish_year"], reverse=False)
    return filtered_books


def save_to_csv(books: List[Dict]) -> None:
    """Save filtered books to a CSV file."""
    fieldnames = [
        "title",
        "author",
        "first_publish_year",
        "edition_count",
    ]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)


def main() -> None:
    books = fetch_books()
    filtered_books = filter_books(books)
    save_to_csv(filtered_books)

    print(f"{len(filtered_books)} books saved successfully")


if __name__ == "__main__":
    main()